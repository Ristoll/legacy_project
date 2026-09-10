import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils import format_date

def test_format_date_valid():
    assert format_date("2026-03-10") == "10.03.2026"

def test_format_date_invalid_slash_input_format():
    assert format_date("2026/03/10") == "2026/03/10"

def test_format_date_invalid_text_date():
    assert format_date("3 жотвня 2026") == "3 жотвня 2026"

def test_format_date__invalid_day():
    assert format_date("2026-03-32") == "2026-03-32"

def test_format_date__invalid_month():
    assert format_date("2026-00-10") == "2026-00-10"

def test_format_date_empty():
    assert format_date("") == ""
