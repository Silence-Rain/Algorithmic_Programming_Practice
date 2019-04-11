import math
import re
import itertools

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0 
    head = ListNode(0)
    currentNode = head
    while l1 or l2:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
            
        currentNode.next = ListNode(carry % 10)
        currentNode = currentNode.next
        carry = carry // 10
        
    if carry == 1:
        currentNode.next = ListNode(1)
        currentNode = currentNode.next
    return head.next

def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    length = 0
    i = 0
    j = 0
    
    while i < len(s) and j < len(s):
        if s[j] not in dic:
            dic[s[j]] = 1
            j += 1
            length = max(length, j - i)  
        else:
            dic.pop(s[i])
            i += 1
    
    return length

def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s

    n = len(s)
    maxLen = 0
    start = 0
    i = 0

    for i in range(0, n):
        if len(s) - i <= maxLen / 2:
            break

        left = i
        right = i
        while right < n - 1 and s[right + 1] == s[right]:
            right += 1

        while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
            right += 1
            left -= 1

        if maxLen < right - left + 1:
            maxLen = right - left + 1
            start = left

    return s[start:maxLen + start]

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    
    mat = [[] for _ in range(numRows)]
    n = len(s)
    for i in range(n):
        size = 2 * (numRows - 1)
        tempInd = i % size
        index = tempInd if tempInd < size / 2 else size - tempInd
        mat[index].append(s[i])
        
    return "".join(["".join(x) for x in mat])

def myAtoi(str: str) -> int:
    match = re.match(r'^(\s*[\+\-]?[0-9]+)[^0-9]+', str)
    INT_MAX = 2 ** 31 - 1
    INT_MIN = - 2 ** 31

    try:
        if match:
            ret = int(match.group(1))
        else:
            ret = int(str)
    except ValueError as e:
        ret = 0

    return INT_MAX if ret > INT_MAX else (ret if ret >= INT_MIN else INT_MIN)

def maxArea(height) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0
    
    while left != right:
        if height[left] < height[right]:
            minHeight = height[left]
            left += 1
        else:
            minHeight = height[right]
            right -= 1
        
        maxArea = max(maxArea, (right - left + 1) * minHeight)

def intToRoman(num: int) -> str:
    mapping = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"]
    ]
    digits = []
    ret = []

    while num >= 1:
        digits.append(num % 10)
        num = int(num / 10)
    
    for ind, i in enumerate(digits):
        print(ind, i)
        ret.append(mapping[ind][i])

    ret.reverse()
    
    return "".join(ret)

def romanToInt(s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ret = 0
        n = len(s)
        
        for i in range(n - 1):
            cur = mapping[s[i]]
            next = mapping[s[i + 1]]
            if cur >= next:
                ret += cur
            else:
                ret -= cur
                
        return ret + mapping[s[n - 1]]

def threeSum(nums: list) -> list:
    res = []
    nums.sort()
    n = len(nums)
    if n == 0 or nums[0] > 0 or nums[n - 1] < 0:
        return []
    for k in range(n):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        target = 0 - nums[k]

        i = k + 1
        j = n - 1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[k], nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

    return res

def letterCombinations(digits: str):
    if len(digits) == 0:
        return []
    
    maps = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    arr = [maps[x] for x in list(digits)]
    return ["".join(x) for x in itertools.product(*arr)]

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    l = ListNode(0)
    l.next = head
    p1 = l
    p2 = l
    
    for i in range(n + 1):
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next
 
    p2.next = p2.next.next
    
    return l.next

def generateParenthesis(n: int) -> list:
    ret = []
    
    def enum(s, lcnt = 0, rcnt = 0):
        if len(s) == 2 * n:
            ret.append(s)
            return
        if lcnt < n:
            enum(s + '(', lcnt + 1, rcnt)
        if rcnt < lcnt:
            enum(s + ')', lcnt, rcnt + 1)

    enum("")
    return ret

def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    temp = ListNode(0)
    bef = temp
    first = temp.next = head
    second = first.next
    
    while second:
        bef.next = second
        first.next = second.next
        second.next = first
        
        bef = first
        first = first.next
        if not first:
            break
        else:
            second = first.next
    
    return temp.next

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

def maximal_square_brute(matrix):
    def getArea(v, k):
        if len(v) < k:
            return 0
        count = 0
        for i in range(len(v)):
            if v[i] != k:
                count = 0
            else:
                count += 1
            if count == k:
                return k ** 2

        return 0

    res = 0
    for i in range(0, len(matrix)):
        v = [0 for x in range(len(matrix[i]))]
        for j in range(i, len(matrix)):
            for k in range(0, len(matrix[j])):
                if matrix[j][k] == '1':
                    v[k] += 1
            res = max(res, getArea(v, j - i + 1))

    return res

def maximal_square_dp(matrix):
    if len(matrix) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    maxi = 0
    dp = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        dp[i][0] = 1 if matrix[i][0] == '1' else 0
        maxi = max(maxi, dp[i][0])
    for i in range(n):
        dp[0][i] = 1 if matrix[0][i] == '1' else 0
        maxi = max(maxi, dp[0][i])

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1 if matrix[i][j] == '1' else 0
            maxi = max(maxi, dp[i][j])

    return maxi ** 2

def perfect_square(n):
    while n % 4 == 0:
        n /= 4

    if n % 8 == 7:
        return 4

    i = 0
    while i ** 2 < n:
        b = int(math.sqrt(n - i ** 2))
        if i ** 2 + b ** 2 == n:
            return 1 if i == 0 else 2

        i += 1

    return 3

def battleship(board):
    if len(board) == 0:
        return 0

    row_len = len(board)
    col_len = len(board[0])
    count = 0

    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                count += 1

    return count

def findMaxLength(nums):
    key = 0
    maxi = 0
    m = {0: -1}

    for i in range(len(nums)):
        key += -1 if nums[i] == 0 else 1
        if key in m:
            maxi = maxi if maxi > i - m[key] else i - m[key]
        else:
            m[key] = i

    return maxi

def valid_square(p1, p2, p3, p4):
    def dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    res = set((dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)))
    return (0 not in res) and len(res) == 2

