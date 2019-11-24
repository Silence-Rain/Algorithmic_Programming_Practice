import re

# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    dic, length, i, j = {}, 0, 0, 0
    while i < len(s) and j < len(s):
        if s[j] not in dic:
            dic[s[j]] = 1
            j += 1
            length = max(length, j - i)  
        else:
            dic.pop(s[i])
            i += 1
    
    return length

# 5. Longest Palindromic Substring
def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s

    n, maxLen, start, i = len(s), 0, 0, 0
    for i in range(0, n):
        if len(s) - i <= maxLen / 2:
            break

        left, right = i, i
        while right < n - 1 and s[right + 1] == s[right]:
            right += 1

        while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
            right += 1
            left -= 1

        if maxLen < right - left + 1:
            maxLen = right - left + 1
            start = left

    return s[start:maxLen + start]

# 6. ZigZag Conversion
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    
    mat, n = [[] for _ in range(numRows)], len(s)
    for i in range(n):
        size = 2 * (numRows - 1)
        tempInd = i % size
        index = tempInd if tempInd < size / 2 else size - tempInd
        mat[index].append(s[i])
        
    return "".join(["".join(x) for x in mat])

# 8. String to Integer (atoi)
def myAtoi(str: str) -> int:
    match, INT_MAX, INT_MIN = re.match(r'^(\s*[\+\-]?[0-9]+)[^0-9]+', str), 2 ** 31 - 1, - (2 ** 31)
    try:
        if match:
            ret = int(match.group(1))
        else:
            ret = int(str)
    except ValueError as e:
        ret = 0

    return INT_MAX if ret > INT_MAX else (ret if ret >= INT_MIN else INT_MIN)

# 22. Generate Parentheses
def generateParenthesis(n: int) -> list:
    def enum(s, lcnt = 0, rcnt = 0):
        if len(s) == 2 * n:
            ret.append(s)
            return
        if lcnt < n:
            enum(s + '(', lcnt + 1, rcnt)
        if rcnt < lcnt:
            enum(s + ')', lcnt, rcnt + 1)

    ret = []
    enum("")

    return ret

# 49. Group Anagrams
def groupAnagrams(strs: list) -> list:
    res = {}
    for item in strs:
        char_map = [0 for _ in range(26)]
        for c in item:
            char_map[ord(c) - 97] += 1

        ind = tuple(char_map)
        if ind not in res:
            res[ind] = [item]
        else:
            res[ind].append(item)
            
    return list(res.values())

# 71. Simplify Path
def simplifyPath(path: str) -> str:
    dirs = path.split('/')
    stack = []
    for i in range(1, len(dirs)):
        if dirs[i] == ".." and len(stack):
            stack.pop()
        elif not len(dirs[i]) or dirs[i] == "." or (dirs[i] == ".." and not len(stack)):
            pass
        else:
            stack.append(dirs[i])

    return "/" + "/".join(stack)

# 165. Compare Version Numbers
def compareVersion(version1: str, version2: str) -> int:
    v1 = [int(v) for v in version1.split(".")]
    v2 = [int(v) for v in version2.split(".")]
    for i in range(max(len(v1), len(v2))):
        t1 = v1[i] if i < len(v1) else 0
        t2 = v2[i] if i < len(v2) else 0
        if t1 > t2:
            return 1
        elif t1 < t2:
            return -1
    
    return 0
