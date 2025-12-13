from abc import ABC, abstractmethod
from typing import List
import unicodedata


class BaseSegmenter(ABC):
    @abstractmethod
    def segment(self, text: str) -> List[str]:
        raise NotImplementedError


class RuleBasedSegmenter(BaseSegmenter):
    def __init__(self, max_length: int):
        self.max_length = max_length
        self.split_tokens = set("。！？!?，,；;：:\n~～….")
        self.dash_tokens = set("—-")

    def _is_symbol(self, ch: str) -> bool:
        cat = unicodedata.category(ch)
        if cat and cat[0] in ("P", "S"):
            return True
        return ch in self.dash_tokens

    def _is_split_trigger(self, ch: str) -> bool:
        if ch in self.dash_tokens:
            return False
        return ch in self.split_tokens

    def _consume_symbol_run(self, text: str, i: int, buffer: List[str]) -> int:
        n = len(text)
        while i < n and self._is_symbol(text[i]):
            buffer.append(text[i])
            i += 1
        return i

    def segment(self, text: str) -> List[str]:
        if not text:
            return []

        segments: List[str] = []
        buffer: List[str] = []

        n = len(text)
        i = 0

        while i < n:
            ch = text[i]

            if not buffer and self._is_symbol(ch):
                tmp: List[str] = []
                i = self._consume_symbol_run(text, i, tmp)
                seg = "".join(tmp).strip()
                if seg:
                    segments.append(seg)
                continue

            buffer.append(ch)

            if self._is_split_trigger(ch):
                i += 1
                i = self._consume_symbol_run(text, i, buffer)

                seg = "".join(buffer).strip()
                if seg:
                    segments.append(seg)
                buffer = []
                continue

            if len(buffer) >= self.max_length:
                i += 1
                i = self._consume_symbol_run(text, i, buffer)

                seg = "".join(buffer).strip()
                if seg:
                    segments.append(seg)
                buffer = []
                continue

            i += 1

        if buffer:
            seg = "".join(buffer).strip()
            if seg:
                segments.append(seg)

        return segments


class SmartSegmenter(BaseSegmenter):
    def __init__(self, max_length: int):
        self.rule_segmenter = RuleBasedSegmenter(max_length)

    def segment(self, text: str) -> List[str]:
        return self.rule_segmenter.segment(text)
