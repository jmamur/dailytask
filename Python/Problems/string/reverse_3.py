#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseStr(s):    
    return ' '.join(s.split()[::-1])[::-1]
