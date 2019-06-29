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

def reverse(x: int) -> int:
    xlist = list(str(x))
    xlist.reverse()
    
    if xlist[-1] == '-':
        xlist.pop()
        xlist.insert(0, '-')
        
    ret = int("".join(xlist))
    return ret if ret >= - 2 ** 31 and ret <= 2 ** 31 - 1 else 0

def isPalindrome_simple(x: int) -> bool:
    s = str(x)
    rev = str(x)[::-1]
    return s == rev

def isPalindrome_no_str(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x = int(x / 10)
        
    return x == reverted or x == int(reverted / 10)

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

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    p1 = l1
    p2 = l2
    res = ListNode(0)
    head = res
    
    while p1 and p2:
        if p1.val <= p2.val:
            res.next = ListNode(p1.val)
            p1 = p1.next
        else:
            res.next = ListNode(p2.val)
            p2 = p2.next
        res = res.next
    
    if p1:
        while p1:
            res.next = ListNode(p1.val)
            p1 = p1.next
            res = res.next
    else:
        while p2:
            res.next = ListNode(p2.val)
            p2 = p2.next
            res = res.next
    
    return head.next

def remove_duplicates(nums):
    i = 0
    j = 0
    count = 0

    while j < len(nums):
        if nums[i] != nums[j]:
            i = j
            count += 1
            nums[count] = nums[i]
        j += 1

    return count + 1

def removeElement(nums: list, val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)

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

def plusOne(digits: list) -> list:
    # return [int(i) for i in str(int("".join(map(str, digits))) + 1)]
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] != 10:
            break
        else:
            digits[i] = 0
    if not digits[0]:
        digits.insert(0, 1)
    return digits

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

def mySqrt(x: int) -> int:
    r = x
    while r * r > x:
        r = (r + x / r) // 2
    return int(r)

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return None
    
    last = head
    p = head.next
    while p:
        if p.val == last.val:
            last.next = p.next
        else:
            last = p
        p = p.next
            
    return head

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

def isSymmetric(root: TreeNode) -> bool:
    def helper(l, r):
        if not l or not r:
            return l == r
        return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)
    
    if not root:
        return True

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def levelOrderBottom(root: TreeNode) -> list:
    if not root:
        return []
    
    q, res = [(root, 0)], []
    while q:
        node, level = q.pop(0)
        if node:
            if level == len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
    
    res.reverse()
    return res

def sortedArrayToBST(nums: list) -> TreeNode:
    n = len(nums)
    if not n:
        return None
    
    mid = n // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    
    return root

def isBalanced(root: TreeNode) -> bool:
    def depth(r):
        if not r:
            return 0
        return 1 + max(depth(r.left), depth(r.right))

    if not root:
        return True
    return abs(depth(root.left) - depth(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    minL = minDepth(root.left) if root.left else float("inf")
    minR = minDepth(root.right) if root.right else float("inf")
    return 1 + min(minL, minR)

def hasPathSum(root: TreeNode, sum: int) -> bool:
    # def dfs(node):
    #     if not node:
    #         return []
    #     res = dfs(node.left)
    #     res += dfs(node.right)
    #     if res:
    #         return [node.val + i for i in res]
    #     else:
    #         return [node.val]
    
    # all_sum = dfs(root)
    # return sum in all_sum
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

def generate(numRows: int) -> list:
    if not numRows:
        return []

    res = [[1]]
    for i in range(1, numRows):
        temp = [1]
        for j in range(i - 1):
            temp.append(res[i - 1][j] + res[i - 1][j + 1])
        res.append(temp + [1])

    return res

def getRow(rowIndex: int) -> list:
    cur = [1]
    for _ in range(rowIndex):
        res = [1]
        for i in range(len(cur) - 1):
            res.append(cur[i] + cur[i + 1])
        res.append(1)
        cur = res
    
    return cur

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

def reverseList(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next, cur = head, head
    
    if not head:
        return None
    
    while cur.next:
        temp = cur.next
        cur.next = temp.next
        temp.next = dummy.next
        dummy.next = temp
        
    return dummy.next

def findShortestSubArray(nums):
    m = {}
    for i,item in enumerate(nums):
        if item in m:
            m[item][0] += 1
            m[item][2] = i
        else:
            m[item] = [1, i, i]

    cur = [0, 0, 0]
    for item in m.values():
        if item[0] > cur[0] or (item[0] == cur[0] and item[2] - item[1] < cur[2] - cur[1]):
            cur = item

    return cur[2] - cur[1] + 1

