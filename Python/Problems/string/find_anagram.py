def findAnagrams(s, p):
    def is_anagram(str1, str2):
        str1 = ''.join(sorted(str1))
        str2 = ''.join(sorted(str2))
        return bool(str1 == str2)
    
    result = []
    n = len(s)
    m = len(p)
    for i in range(0, n-m+1):
        step = i + m
        if is_anagram(p, s[i:step]):
            result.append(i)
    return result


        
