"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. checks if they are
one edit (or zero edits) away.
"""


def oneway(stra, strb):
    if abs(len(stra) - len(strb)) > 1:
        return False
    longer = ''.join(sorted(stra)) if len(stra) > len(strb) else ''.join(sorted(strb))
    shorter = ''.join(sorted(stra)) if len(stra) < len(strb) else ''.join(sorted(strb))
    bucket = [ ltr for ltr in longer if ltr not in shorter ]
    if len(bucket) > 1:
        return False
    return True


    
