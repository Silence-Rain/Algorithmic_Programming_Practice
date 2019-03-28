import math
import re

class ListNode:
    pass

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
