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

def inorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    
    res = []
    res += inorderTraversal(root.left)
    res.append(root.val)
    res += inorderTraversal(root.right)
    
    return res

def levelOrder(root: TreeNode) -> list:
    if not root:
        return []

    q = [(root, 0)]
    res = []
    while q:
        node, level = q.pop(0)
        if node:
            if len(res) < level + 1:
                res.append([node.val])
            else:
                res[level].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
    
    return res

def zigzagLevelOrder(root: TreeNode) -> list:
    if not root:
        return []

    q = [(root, 0)]
    res = []
    flag = True
    while q:
        for i in range(len(q)):
            if flag:
                node, level = q.pop(0)
                if node:
                    if len(res) < level + 1:
                        res.append([node.val])
                    else:
                        res[level].append(node.val)
                    q.append((node.left, level + 1))
                    q.append((node.right, level + 1))
            else:
                node, level = q.pop()
                if node:
                    if len(res) < level + 1:
                        res.append([node.val])
                    else:
                        res[level].append(node.val)
                    q.insert(0, (node.right, level + 1))
                    q.insert(0, (node.left, level + 1))
        
        flag = not flag
   
    return res

def buildTree(preorder: list, inorder: list) -> TreeNode:
    if not preorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    ind = inorder.index(root_val)
    root.left = buildTree(preorder[:ind], inorder[:ind])
    root.right = buildTree(preorder[ind:], inorder[ind + 1:])
    
    return root

 def buildTree(inorder: list, postorder: list) -> TreeNode:
    if not postorder:
        return None
        
    root_val = postorder.pop()
    root = TreeNode(root_val)
    ind = inorder.index(root_val)
    root.left = buildTree(inorder[:ind], postorder[:ind])
    root.right = buildTree(inorder[ind + 1:], postorder[ind:])
    
    return root

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

def pathSum(root: TreeNode, sum: int) -> list:
    def dfs(node):
        if not node:
            return []
        res = dfs(node.left)
        res += dfs(node.right)
        if res:
            res = [[node.val] + i for i in res]
        else:
            res = [[node.val]]
        return res
    
    all_paths = dfs(root)
    ret = []
    for i in all_paths:
        s = 0
        for j in i:
            s += j
        if s == sum:
            ret.append(i)
    
    return ret

def connect(root: 'Node') -> 'Node':
    if not root:
        return None

    cur = root
    while cur.left:
        next = cur.left
        while cur:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next

        cur = next

    return root

def connect(root: 'Node') -> 'Node':
    cur, head, tail = root, None, None

    while cur:
        while cur:
            if cur.left:
                if not head:
                    head = cur.left
                    tail = head
                else:
                    tail.next = cur.left
                    tail = tail.next
            if cur.right:
                if not head:
                    head = cur.right
                    tail = head
                else:
                    tail.next = cur.right
                    tail = tail.next
                    
            cur = cur.next

        cur = head
        head, tail = None, None

    return root

def sumNumbers(root: TreeNode) -> int:
    def dfs(node):
        if not node:
            return []
        res = dfs(node.left)
        res += dfs(node.right)
        if res:
            ret = ["%s%s" % (node.val, i) for i in res]
        else:
            ret = [str(node.val)]
        
        return ret

    paths = dfs(root)
    s = 0
    for item in paths:
        s += int(item)
    return s

def singleNumber(nums: list) -> int:
    ones, twos = 0, 0
    for i in nums:
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones
    
    return ones

def preorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    res = [root.val]
    res += self.preorderTraversal(root.left)
    res += self.preorderTraversal(root.right)
    
    return res

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

