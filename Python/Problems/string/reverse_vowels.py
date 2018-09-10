#Write a function that takes a string as input and reverse only the vowels of a string.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def reverseVowels(s):    
    n = len(s)
    s = list(s)
    sp = 0
    ep = n - 1
    while sp < ep:
        if s[sp] in VOWELS and s[ep] in VOWELS:
            s[sp], s[ep] = s[ep], s[sp]
            sp += 1                
            ep -= 1
        elif s[sp] not in VOWELS:
            sp += 1
        elif s[ep] not in VOWELS:
            ep -= 1
        
    return ''.join(s)

string = 'ai' 
print(reverseVowels(string))


