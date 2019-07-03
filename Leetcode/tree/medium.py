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

# 94. Binary Tree Inorder Traversal
def inorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    
    res = inorderTraversal(root.left)
    res.append(root.val)
    res += inorderTraversal(root.right)
    
    return res

# 102. Binary Tree Level Order Traversal
def levelOrder(root: TreeNode) -> list:
    if not root:
        return []

    q, res = [(root, 0)], []
    while q:
        node, level = q.pop(0)
        if node:
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
    
    return res

# 103. Binary Tree Zigzag Level Order Traversal
def zigzagLevelOrder(root: TreeNode) -> list:
    if not root:
        return []

    q, res, flag = [(root, 0)], [], True
    while q:
        for i in range(len(q)):
            if flag:
                node, level = q.pop(0)
                if node:
                    if len(res) == level:
                        res.append([node.val])
                    else:
                        res[level].append(node.val)
                    q.append((node.left, level + 1))
                    q.append((node.right, level + 1))
            else:
                node, level = q.pop()
                if node:
                    if len(res) == level:
                        res.append([node.val])
                    else:
                        res[level].append(node.val)
                    q.insert(0, (node.right, level + 1))
                    q.insert(0, (node.left, level + 1))
        
        flag = not flag
   
    return res

# 105. Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(preorder: list, inorder: list) -> TreeNode:
    if not preorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    ind = inorder.index(root_val)
    root.left = buildTree(preorder[:ind], inorder[:ind])
    root.right = buildTree(preorder[ind:], inorder[ind + 1:])
    
    return root

# 106. Construct Binary Tree from Inorder and Postorder Traversal
 def buildTree(inorder: list, postorder: list) -> TreeNode:
    if not postorder:
        return None
        
    root_val = postorder.pop()
    root = TreeNode(root_val)
    ind = inorder.index(root_val)
    root.left = buildTree(inorder[:ind], postorder[:ind])
    root.right = buildTree(inorder[ind + 1:], postorder[ind:])
    
    return root

# 113. Path Sum II
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

# 116. Populating Next Right Pointers in Each Node
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

# 117. Populating Next Right Pointers in Each Node II
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

# 129. Sum Root to Leaf Numbers
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

# 144. Binary Tree Preorder Traversal
def preorderTraversal(root: TreeNode) -> list:
    if not root:
        return []

    res = [root.val]
    res += self.preorderTraversal(root.left)
    res += self.preorderTraversal(root.right)
    
    return res