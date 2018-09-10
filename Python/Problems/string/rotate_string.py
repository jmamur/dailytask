#We are given two strings, A and B.

#A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
# Return True if and only if A can become B after some number of shifts on A.
#A and B will have length at most 100.

def rotateString(A, B):    
    n = len(A)
    m = len(B)
    if n != m:
        return False
    tmp = list(A) + list(A)
    B = list(B)
    if B in tmp:
        return True
    return False


