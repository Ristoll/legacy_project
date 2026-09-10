# tests/test_characterization.py
# Tests for checking behaviour of format_date() function

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils import format_date


def test_format_date_valid():
    assert format_date("2026-03-10") == "10.03.2026"


def test_format_date_invalid_slash_input_format():
    with pytest.raises(ValueError, match="Invalid date formatting"):
        format_date("2026/10/10")


def test_format_date_invalid_text_date():
    with pytest.raises(ValueError, match="Invalid date formatting"):
        format_date("3 жовтня 2026")


def test_format_date_invalid_day():
    with pytest.raises(ValueError, match="Invalid date formatting"):
        format_date("2026-03-32")


def test_format_date_invalid_month():
    with pytest.raises(ValueError, match="Invalid date formatting"):
        format_date("2026-00-10")


def test_format_date_empty():
    with pytest.raises(ValueError, match="Invalid date formatting"):
        format_date("")