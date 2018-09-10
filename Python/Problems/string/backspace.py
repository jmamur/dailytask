#Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# # means a backspace character.

#Input: S = "ab#c", T = "ad#c"
#Output: true
#Explanation: Both S and T become "ac".

def backspaceCompare(S, T):
    def clear(S):
        stck = []
        for c in S:
            if c != '#':
                stck.append(c)
            elif stck:
                stck.pop()
        return stck
    return clear(S) == clear(T)

print(backspaceCompare("a#c", "b"))
print(backspaceCompare("a##c", "#a#c"))