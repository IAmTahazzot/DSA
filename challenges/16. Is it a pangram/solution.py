"""
# Check whether a given string is a pangram or not
"""

import string


def is_pangram(s: str) -> bool:
    return all([c in s.lower() for c in string.ascii_lowercase])
