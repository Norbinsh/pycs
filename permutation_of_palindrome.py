"""
Checks if given string is a permutation of palindrome
"""


def chk(s):
    s = s.replace(" ", "")
    s = s.lower()

    d = dict()

    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    odds = 0

    for k,v in d.items():
        if v % 2 != 0 and odds == 0:
            odds += 1
        elif v % 2 != 0 and odds != 0:
            return False
    return True
    
print(chk("racecar")) # true 