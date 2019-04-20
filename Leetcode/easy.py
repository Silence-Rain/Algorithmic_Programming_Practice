class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def twosum(nums, target):
    dic = {}
    for i, item in enumerate(nums):
        if item in dic:
            dic[item].append(i)
        else:
            dic[item] = [i]

    nums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            if nums[i] == nums[j]:
                return dic[nums[i]]
            else:
                return [dic[nums[i]][0], dic[nums[j]][0]]


        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

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

def searchInsert(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    if target > nums[-1]:
        return right + 1
    if target < nums[0]:
        return left
    
    while left <= right:
        mid = round((left + right) / 2)
        if nums[mid] == target:
            return mid
        elif mid < len(nums) - 1 and nums[mid] < target <= nums[mid + 1]:
            return mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

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

