from typing import Optional
from urllib.parse import urlparse, urlunparse

ALLOWED_SCHEMES = {"http", "https"}


def sanitize_base_url(value: Optional[str]) -> str:
    """
    Normalize a provided base URL to a safe http(s) root without trailing slash,
    and drop query/fragment data. Returns empty string if the input is invalid.
    """
    raw = (value or "").strip()
    if not raw:
        return ""
    try:
        parsed = urlparse(raw)
    except Exception:
        return ""
    if parsed.scheme not in ALLOWED_SCHEMES or not parsed.netloc:
        return ""
    path = (parsed.path or "").rstrip("/")
    sanitized = parsed._replace(path=path, params="", query="", fragment="")
    return urlunparse(sanitized)
