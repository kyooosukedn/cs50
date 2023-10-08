import unittest
from twttr import shorten

def test_shorten_empty_strings():
    assert shorten("") == ""

def test_shorten_no_vowels():
    assert shorten("twttr") == "twttr"

def test_shorten_all_vowels():
    assert shorten("aeiueo") == ""

def test_shorten_mixed_characters():
    assert shorten("abcdefg") == "bcdfg"

if __name__ == "__main__":
    unittest.main()
