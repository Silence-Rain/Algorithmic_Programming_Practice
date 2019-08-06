class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2. Add Two Numbers
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head, carry = ListNode(0), 0
    cur = head
    while l1 or l2:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
            
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry = carry // 10
        
    if carry == 1:
        cur.next = ListNode(1)
        cur = cur.next

    return head.next

# 19. Remove Nth Node From End of List
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    l = ListNode(0)
    l.next, p1, p2 = head, l, l
    
    for i in range(n + 1):
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next
 
    p2.next = p2.next.next
    
    return l.next

# 24. Swap Nodes in Pairs
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

# 61. Rotate List
def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or not k:
        return head
    
    tail, n = head, 1
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

# 82. Remove Duplicates from Sorted List II
def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return None
    
    res, last, p = set(), head, head.next
    while p:
        if p.val == last.val:
            last.next = p.next
            res.add(p.val)
        else:
            last = p
        p = p.next
    
    dummy = ListNode(0)
    dummy.next = head
    last, p = dummy, head
    while p:
        if p.val in res:
            last.next = p.next
        else:
            last = last.next
        p = p.next
        
    return dummy.next

# 92. Reverse Linked List II
def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    cnt, cur, beg, end = 0, dummy, None, None
    
    while cur and cnt < m - 1:
        cnt += 1
        cur = cur.next
    
    beg, cur, i = cur, cur.next, 0
    while cur.next and i < n - m:
        temp = cur.next
        cur.next = temp.next
        temp.next = beg.next
        beg.next = temp
        i += 1
    
    return dummy.next

# 109. Convert Sorted List to Binary Search Tree
def sortedListToBST(head: ListNode) -> TreeNode:
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    
    pfast, pslow, pre = head, head, None
    while pfast and pfast.next:
        pre = pslow
        pfast = pfast.next.next
        pslow = pslow.next
    
    pre.next = None
    root = TreeNode(pslow.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(pslow.next)
    
    return root

# 147. Insertion Sort List
def insertionSortList(head: ListNode) -> ListNode:
    dummy, p = ListNode(0), head
    while p:
        temp, pre = p.next, dummy
        while pre.next and pre.next.val < p.val:
            pre = pre.next

        p.next = pre.next
        pre.next = p
        p = temp
    
    return dummy.next