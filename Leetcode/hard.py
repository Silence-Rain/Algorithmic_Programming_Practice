import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

def isNumber(s: str) -> bool:
    def isSign(s):
        return s == '+' or s == '-'
    
    def isUnsignedInt(s):
        if not len(s):
            return False
        
        for i in s:
            if ord(i) < 48 or ord(i) > 57:
                return False
        return True
    
    def isSignedInt(s):
        if not len(s):
            return False
        s = s[1:] if isSign(s[0]) else s
        
        return isUnsignedInt(s)
    
    def isDecimals(s):
        if not len(s):
            return False
        s_dot = s.split('.')
        
        if len(s_dot) > 2:
            return False
        if len(s_dot) == 1:
            return isSignedInt(s)
        
        if len(s_dot[0]):
            if len(s_dot[1]):
                return (isSignedInt(s_dot[0]) or isSign(s_dot[0])) and isUnsignedInt(s_dot[1])
            else:
                return isSignedInt(s_dot[0])
        else:
            if len(s_dot[1]):
                return isUnsignedInt(s_dot[1])
            else:
                return False
    
    s = s.strip()
    s_e = s.split('e')
    
    if len(s_e) > 2:
        return False
    if len(s_e) == 1:
        return isDecimals(s)
    
    return isDecimals(s_e[0]) and isSignedInt(s_e[1])
        
def postorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    
    res = self.postorderTraversal(root.left)
    res += self.postorderTraversal(root.right)
    res.append(root.val)
    
    return res
