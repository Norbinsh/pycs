"""
An algorithm to determine if a string has all unique characters.
"""

def is_unique(data_str):
    bucket = [

    ]

    for ltr in data_str:
        if ltr in bucket:
            return False
        bucket.append(ltr)
    return True

# If you could not use other data structures (such as the list we used), we could either:
# 1. sort the string and check adjacent similar letters
# 2. additional way (IF you could use a set) was to check the input length, perform a set, and check the length equals


