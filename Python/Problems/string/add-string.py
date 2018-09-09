#Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

def addStrings(num1, num2):
    n = len(num1) - 1
    m = len(num2) - 1
    
    carry = 0
    result = str()
    while(n >= 0 or m >= 0 or carry > 0):
        tmp_sum = 0
        if n >=0 :
            tmp_sum += int(num1[n])
            n -= 1
        if m >= 0:
            tmp_sum += int(num2[m])
            m -= 1
        
        tmp_sum += carry
        carry = tmp_sum // 10
        tmp_sum %= 10 
        result += str(tmp_sum)
    
    result = result[::-1]
    return result

print(addStrings("1", "1"))