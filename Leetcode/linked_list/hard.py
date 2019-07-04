class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 23. Merge k Sorted Lists
def mergeKLists(lists: list) -> ListNode:
    n = len(lists)
    head = res = ListNode(0)
    
    while True:
        min_ind, min_val = -1, None
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

# 25. Reverse Nodes in k-Group
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def rev(pre: ListNode, next: ListNode):
        last, cur = pre.next, last.next
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
            
        return last

    if not head or k == 1:
        return head

    temp = ListNode(0)
    temp.next, pre, cur, i = head, temp, head, 1
    while cur:
        if (i % k == 0):
            pre = rev(pre, cur.next)
            cur = pre.next
        else:
            cur = cur.next
        i += 1

    return temp.next