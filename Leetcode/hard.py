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
