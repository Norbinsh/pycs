"""
Replaces spaces with a url encoding of '%20'
"""

def urlify(s):
    return s.replace(" ", "%20")

print(urlify("https://www.google.com/search?source=hp&ei=n-nuXPj-GYvjsAfFxpqwDA&q=hello there"))

# https://www.google.com/search?source=hp&ei=n-nuXPj-GYvjsAfFxpqwDA&q=hello there