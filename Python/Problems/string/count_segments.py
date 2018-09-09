
def countSegments(s):
    """
    :type s: str
    :rtype: int
    """
    cnt = 0
    n = len(s)
    if n == 0:
        return 0
    for i in range(0, n):
        if (s[i] == ' ' or i == 0 )and s[i-1] != ' ':
            cnt += 1
    return cnt