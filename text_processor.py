"""Text processing utilities for Project Gutenberg text slicing.

This module provides functions for normalizing, slicing, and locating
text boundaries in Project Gutenberg files.
"""

from typing import Tuple


def get_anchor_index(text: str, marker: str, is_start: bool = True) -> Tuple[int, int]:
    """Find the index of a text marker with fallback to first/last line matching.

    When an exact match of the marker string cannot be found, this function
    falls back to matching just the first (or last) non-empty line of the marker.
    This is useful when LLM-extracted markers have minor encoding or whitespace
    differences from the original text.

    Args:
        text: The full text to search within.
        marker: The substring to locate (may be multi-line).
        is_start: If True, search from start (find); if False, search from end (rfind).

    Returns:
        A tuple of (index, length) where:
        - index: The position of the marker in text (or first/last line), or -1 if not found.
        - length: The length of the match (full marker or fallback line).

    Example:
        >>> text = "Chapter 1\\n\\nOnce upon a time..."
        >>> marker = "Chapter 1"
        >>> idx, length = get_anchor_index(text, marker, is_start=True)
        >>> idx
        0
        >>> length
        9
    """
    # Try the full verbatim match first
    idx = text.find(marker) if is_start else text.rfind(marker)

    if idx == -1:
        # Fallback: match just the first (or last) non-empty line of the marker
        lines = [line for line in marker.split("\n") if line.strip()]
        if not lines:
            return -1, 0

        anchor = lines[0] if is_start else lines[-1]
        idx = text.find(anchor) if is_start else text.rfind(anchor)
        return idx, len(anchor)

    return idx, len(marker)
