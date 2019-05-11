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

def nextPermutation(nums: list) -> None:
    n = len(nums)
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            # find first larger element in i - n
            cur_max = None
            cur_ind = None
            for j in range(i - 1, n):
                if nums[j] > nums[i - 1]:
                    if not cur_max or nums[j] <= cur_max:
                        cur_max = nums[j]
                        cur_ind = j
            # swap them
            temp = nums[i - 1]
            nums[i - 1] = nums[cur_ind]
            nums[cur_ind] = temp
            # sort i~n in ascending order (reverse)
            l = i
            r = n - 1
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                
                l += 1
                r -= 1          
            return
        
    nums.sort()
    return

def search(nums: list, target: int) -> int:        
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = round((left + right) / 2)     
        if nums[mid] == target:
            return mid     
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def searchRange(nums: list, target: int) -> list:
    left = 0
    right = len(nums) - 1
    res = [-1, -1]
    
    while left <= right:
        mid = round((left + right) / 2)
        if nums[mid] == target:
            cur_l = cur_r = mid
            while cur_l > 0 and nums[cur_l - 1] == target:
                cur_l -= 1
            while cur_r < len(nums) - 1 and nums[cur_r + 1] == target:
                cur_r += 1
            res = [cur_l, cur_r]
            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return res

def isValidSudoku(board: list) -> bool:
    rows = [{} for i in range(9)]
    cols = [{} for i in range(9)]
    boxes = [{} for i in range(9)]
    
    for i in range(9):
        for j in range(9):
            elem = board[i][j]
            if elem != ".":
                if elem in rows[i] or elem in cols[j] or elem in boxes[3 * (i // 3) + j // 3]:
                    return False
                else:
                    rows[i][elem] = 1
                    cols[j][elem] = 1
                    boxes[3 * (i // 3) + j // 3][elem] = 1
    
    return True    

def permute(nums: list) -> list:
    if len(nums) <= 1:
        return [nums]
    
    res = []
    temp = self.permute(nums[1:])
    for item in temp:
        for i in range(len(item) + 1):
            res.append(item[:i] + [nums[0]] + item[i:])
    
    return res

def rotate(matrix: list) -> None:
    # n = len(matrix)
    # for i in range(math.ceil(n/2)):
    #     for j in range(math.floor(n/2)):
    #         temp = matrix[i][j]
    #         matrix[i][j] = matrix[n - 1 - j][i]
    #         matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
    #         matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i] 
    #         matrix[j][n - 1 - i] = temp
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

def spiralOrder(matrix: list) -> list:
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    cnt = min(m, n) // 2 + 1 if min(m, n) % 2 else min(m, n) // 2
    ret = []
    
    for i in range(cnt):
        ret.extend(matrix[i][i:n - i])
        for j in range(i + 1, m - i):
            ret.append(matrix[j][n - i - 1])
        if i + 1 != m - i and i + 1 != n - i:
            ret.extend(matrix[m - i - 1][i:n - i - 1][::-1])
            for j in range(m - i - 2, i, -1):
                ret.append(matrix[j][i])

    return ret

def merge(intervals: list) -> list:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    ret = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= ret[-1][1]:
            ret[-1][1] = max(ret[-1][1], intervals[i][1])
        else:
            ret.append(intervals[i])
    
    return ret

def generateMatrix(n: int) -> list:
    def indexGenerator(n, start):
        if n == 0:
            return
        if n == 1:
            yield start, start
        else:
            for i in range(n):
                yield start, start + i
            for i in range(1, n):
                yield start + i, start + n - 1
            for i in range(1, n):
                yield start + n - 1, start + n - 1 - i
            for i in range(1, n - 1):
                yield start + n - 1 - i, start
            for i, j in indexGenerator(n - 2, start + 1):
                yield i, j
    
    ret = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    for i, j in indexGenerator(n, 0):
        ret[i][j] = cnt
        cnt += 1
    
    return ret

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or not k:
        return head
    
    tail = head
    n = 1
    while tail.next:
        tail = tail.next
        n += 1
        
    diff = k % n
    if not diff:
        return head
    else:
        p = head
        for i in range(n - diff - 1):
            p = p.next

        last = p
        p = p.next
        last.next = None
        ret = p
        while p.next:
            p = p.next
        p.next = head

        return ret

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

def searchMatrix(matrix: list, target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    rl, rh = 0, m - 1
    cl, ch = 0, n - 1
    targetRow = -1
    
    while rl <= rh:
        rmid = (rl + rh) // 2
        if matrix[rmid][0] == target:
            return True
        elif matrix[rmid][0] > target:
            if not rmid:
                return False
            elif target > matrix[rmid - 1][0]:
                targetRow = rmid - 1
                break
            else:
                rh = rmid - 1
        else:
            if rmid == m - 1:
                targetRow = m - 1
                break
            elif target < matrix[rmid + 1][0]:
                targetRow = rmid
                break
            else:
                rl = rmid + 1
    
    while cl <= ch:
        cmid = (cl + ch) // 2
        if matrix[targetRow][cmid] == target:
            return True
        elif matrix[targetRow][cmid] > target:
            ch = cmid - 1
        else:
            cl = cmid + 1
    
    return False

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

