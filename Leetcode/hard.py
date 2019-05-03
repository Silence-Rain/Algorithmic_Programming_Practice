import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    res = []
    flag = (m + n) % 2 == 1
    cnt = math.ceil((m + n) / 2) if flag else int((m + n) / 2 + 1)
    
    for i in range(0, cnt):
        if len(nums1) == 0:
            res.append(nums2.pop(0))
        elif len(nums2) == 0:
            res.append(nums1.pop(0))
        else:
            if nums1[0] >= nums2[0]:
                res.append(nums2.pop(0))
            else:
                res.append(nums1.pop(0))

    return float(res[-1]) if flag else (res[-2] + res[-1]) / 2.0

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def rev(pre: ListNode, next: ListNode):
        last = pre.next
        cur = last.next
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last

    if not head or k == 1:
        return head

    temp = ListNode(0)
    temp.next = head
    pre = temp
    cur = head

    i = 1
    while cur:
        if (i % k == 0):
            pre = rev(pre, cur.next)
            cur = pre.next
        else:
            cur = cur.next
        i += 1

    return temp.next

def mergeKLists(lists: list) -> ListNode:
    n = len(lists)
    head = res = ListNode(0)
    
    while True:
        min_ind = -1
        min_val = None
        for i in range(0, n):
            if not lists[i]:
                continue          
            if min_val is None or lists[i].val <= min_val:
                min_ind = i
                min_val = lists[i].val
                
        if min_ind == -1:
            break
        
        res.next = ListNode(min_val)
        res = res.next
        lists[min_ind] = lists[min_ind].next

    return head.next

def findSubstring(s: str, words: list) -> list:
    s_l = len(s)
    ws_l = len(words)
    ret = []
    if not s_l or not ws_l:
        return []
    
    w_l = len(words[0])
    words_map = {}
    for item in words:
        if item in words_map:
            words_map[item] += 1
        else:
            words_map[item] = 1
    
    for i in range(s_l - w_l * ws_l + 1):
        w_map_temp = words_map.copy()
        if s[i:i + w_l] in w_map_temp:
            flag = True
            for j in range(ws_l):
                temp_str = s[i + w_l * j:i + w_l * (j + 1)]  
                if temp_str in w_map_temp and w_map_temp[temp_str] != 0:
                    w_map_temp[temp_str] -= 1
                else:
                    flag = False
                    break
            
            if flag:
                ret.append(i)
                
    return ret

def firstMissingPositive(nums: list) -> int:
        n = len(nums)
        flags = [False for _ in range(n + 1)]
        
        for i in range(n):
            if nums[i] > n:
                continue
            if nums[i] > 0:
                flags[nums[i] - 1] = True
                
        for i in range(len(flags)):
            if flags[i] == False:
                return i + 1

def insert(intervals: list, newInterval: list) -> list:
    left, right = [], []
    start, end = newInterval[0], newInterval[1]
    
    for i in intervals:
        if i[1] < start:
            left.append(i)
        elif i[0] > end:
            right.append(i)
        else:
            start = min(i[0], start)
            end = max(i[1], end)
    
    return left + [[start, end]] + right


