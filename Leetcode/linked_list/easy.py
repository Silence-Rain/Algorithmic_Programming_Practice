class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 21. Merge Two Sorted Lists
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    res = ListNode(0)
    head, p1, p2 = res, l1, l2
    
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

# 83. Remove Duplicates from Sorted List
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

# 206. Reverse Linked List
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