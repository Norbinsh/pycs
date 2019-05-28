"""
Check Permutation: decide if one is a permutation of the other.
"""

def is_permutation(first: str, second: str) -> bool:
    # If the length of both strings isn't equal, we return immediately
    if len(first) != len(second):
        return False
    # After sorting, both strings should be equal
    if ''.join(sorted(first)) != ''.join(sorted(second)):
        return False
    return True

