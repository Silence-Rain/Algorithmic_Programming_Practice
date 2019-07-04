import re

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestCommonPrefix(strs: list) -> str:
    ind = 0
    n = len(strs)
    
    if n == 0:
        return ""
    elif n == 1:
        return strs[0]
    else:
        try:
            while True:
                for i in range(1, n):
                    if strs[i - 1][ind] != strs[i][ind]:
                        return strs[0][:ind]
                ind += 1
        except:
            return strs[0][:ind]

def isValid(s: str) -> bool:
    front = ["{", "[", "("]
    back = ["}", "]", ")"]
    strs = list(s)
    
    if not len(strs):
        return True
    if len(strs) == 1 or strs[0] in back:
        return False
    
    stack = [strs.pop(0)]
    while len(strs):
        cur = strs.pop(0)
        if cur in front:
            stack.append(cur)
        elif not len(stack) or front.index(stack[-1]) != back.index(cur):
            return False
        else:
            stack.pop()
            
    return False if len(stack) else True

def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    
    prev = countAndSay(n - 1)
    ret = ""
    c = 0
    for i in range(len(prev)):
        c += 1
        
        if i + 1 == len(prev) or prev[i] != prev[i + 1]:
            ret += "%s%s" % (c, prev[i])
            c = 0
    
    return ret

def lengthOfLastWord_regexp(s: str) -> int:
    return len(re.search(r"([a-zA-Z] )*([a-zA-Z]+)[ ]*$", s).group(2)) if len(s.strip()) else 0

def lengthOfLastWord_split(s: str) -> int:
    return len(s.strip().split(" ")[-1])

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

def singleNumber(nums: list) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res

