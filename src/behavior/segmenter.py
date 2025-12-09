"""
Message Segmentation Module

Provides interface for message segmentation with both mini-model and rule-based implementations.
"""
from abc import ABC, abstractmethod
from typing import List, Optional

import httpx


class BaseSegmenter(ABC):
    """Abstract base class for message segmentation"""

    @abstractmethod
    def segment(self, text: str) -> List[str]:
        """
        Segment a message into natural chunks.

        Args:
            text: Input message text

        Returns:
            List of text segments
        """
        raise NotImplementedError


class RuleBasedSegmenter(BaseSegmenter):
    """
    Rule-based segmenter using punctuation and dash characters.
    This serves as a fallback and baseline until the mini model is ready.
    """

    def __init__(self, max_length: int = 60):
        self.max_length = max_length
        self.split_tokens = set("。，．,.！？!?、；;—-－")

    def segment(self, text: str) -> List[str]:
        """Segment text using punctuation boundaries and optional length guard."""
        if not text:
            return []

        segments: List[str] = []
        buffer: List[str] = []

        for char in text:
            buffer.append(char)
            should_split = char in self.split_tokens

            if not should_split and len(buffer) < self.max_length:
                continue

            segment = "".join(buffer).strip()
            if segment:
                segments.append(segment)
            buffer = []

        if buffer:
            remaining = "".join(buffer).strip()
            if remaining:
                segments.append(remaining)

        return segments


class MiniModelSegmenter(BaseSegmenter):
    """
    HTTP-based mini model caller. Expects an endpoint that returns {"segments": [...]}
    """

    def __init__(self, endpoint: str, timeout: float = 2.0):
        self.endpoint = endpoint
        self.timeout = timeout

    def segment(self, text: str) -> List[str]:
        if not text:
            return []

        try:
            response = httpx.post(
                self.endpoint,
                json={"text": text},
                timeout=self.timeout,
            )
            response.raise_for_status()
            payload = response.json()
            segments = payload.get("segments")
            if not isinstance(segments, list):
                raise ValueError("mini model response missing 'segments' list")

            cleaned = [str(s).strip() for s in segments if str(s).strip()]
            if not cleaned:
                raise ValueError("mini model returned no usable segments")

            return cleaned
        except Exception as exc:
            raise RuntimeError(f"Mini model segmentation failed: {exc}") from exc


class SmartSegmenter(BaseSegmenter):
    """
    Smart segmenter that automatically chooses between mini-model and rule-based
    segmentation based on availability.
    """

    def __init__(
        self,
        max_length: int = 60,
        use_mini_model: bool = False,
        mini_model_endpoint: Optional[str] = None,
        mini_model_timeout: float = 2.0,
    ):
        self.rule_segmenter = RuleBasedSegmenter(max_length)
        self.mini_model: Optional[MiniModelSegmenter] = None

        if use_mini_model and mini_model_endpoint:
            self.mini_model = MiniModelSegmenter(
                endpoint=mini_model_endpoint,
                timeout=mini_model_timeout,
            )

    def segment(self, text: str) -> List[str]:
        """Use mini model if available, otherwise fall back to rules."""
        if self.mini_model:
            try:
                return self.mini_model.segment(text)
            except Exception as exc:
                print(f"[behavior] mini model unavailable, fallback to rules: {exc}")

        return self.rule_segmenter.segment(text)
