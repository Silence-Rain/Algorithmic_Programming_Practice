import math
import re
import itertools

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return None
    
    res = set()
    last = head
    p = head.next
    while p:
        if p.val == last.val:
            last.next = p.next
            res.add(p.val)
        else:
            last = p
        p = p.next
    
    dummy = ListNode(0)
    dummy.next = head
    last = dummy
    p = head
    while p:
        if p.val in res:
            last.next = p.next
        else:
            last = last.next
        p = p.next
        
    return dummy.next

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    cnt, cur, beg, end = 0, dummy, None, None
    
    while cur and cnt < m - 1:
        cnt += 1
        cur = cur.next
    
    beg = cur
    cur = cur.next
    i = 0
    while cur.next and i < n - m:
        temp = cur.next
        cur.next = temp.next
        temp.next = beg.next
        beg.next = temp
        i += 1
    
    return dummy.next

def sortedListToBST(head: ListNode) -> TreeNode:
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    
    pfast = head
    pslow = head
    pre = None
    while pfast and pfast.next:
        pre = pslow
        pfast = pfast.next.next
        pslow = pslow.next
    
    pre.next = None
    root = TreeNode(pslow.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(pslow.next)
    
    return root

def singleNumber(nums: list) -> int:
    ones, twos = 0, 0
    for i in nums:
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones
    
    return ones

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

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

