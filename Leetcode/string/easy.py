import re

# 14. Longest Common Prefix
def longestCommonPrefix(strs: list) -> str:
    ind, n = 0, len(strs)
    
    if n == 0:
        return ""
    if n == 1:
        return strs[0]

    try:
        while True:
            for i in range(1, n):
                if strs[i - 1][ind] != strs[i][ind]:
                    return strs[0][:ind]
            ind += 1
    except:
        return strs[0][:ind]

# 20. Valid Parentheses
def isValid(s: str) -> bool:
    l, r, s_list = {'(':0, '{':1, '[':2}, {')':0, '}':1, ']':2}, list(s)
    if not s:
        return True
    if s[0] in r:
        return False
        
    stack = [s_list.pop(0)]
    while s_list:
        cur = s_list.pop(0)
        if cur in l:
            stack.append(cur)
        elif stack:
            if stack[-1] in r:
                return False
            elif l[stack[-1]] != r[cur]:
                return False
            else:
                stack.pop()
        else:
            return False
            
    return not stack

# 28. Implement strStr()
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

# 38. Count and Say
def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    
    prev, ret, c = countAndSay(n - 1), "", 0
    for i in range(len(prev)):
        c += 1        
        if i + 1 == len(prev) or prev[i] != prev[i + 1]:
            ret += "%s%s" % (c, prev[i])
            c = 0
    
    return ret

# 58. Length of Last Word
def lengthOfLastWord_1(s: str) -> int:
    return len(re.search(r"([a-zA-Z] )*([a-zA-Z]+)[ ]*$", s).group(2)) if len(s.strip()) else 0
def lengthOfLastWord_2(s: str) -> int:
    return len(s.strip().split(" ")[-1])

# 67. Add Binary
def addBinary(a: str, b: str) -> str:
    la, lb = len(a), len(b)
    if la > lb:
        b = "0" * (la - lb) + b
    elif la < lb:
        a = "0" * (lb - la) + a
        
    res = ""
    carry = 0
    for i in range(max(la, lb) - 1, -1, -1):
        temp_sum = int(a[i]) ^ int(b[i])
        temp_carry = int(a[i]) & int(b[i])
        res = str(temp_sum ^ carry) + res
        carry = (temp_sum & carry) | temp_carry
    
    return res if not carry else "1" + res

# 125. Valid Palindrome
def isPalindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i] != s[j] and s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True
