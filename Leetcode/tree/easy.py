class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 100. Same Tree
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

# 101. Symmetric Tree
def isSymmetric(root: TreeNode) -> bool:
    def helper(l, r):
        if not l or not r:
            return l == r
        return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)
    
    if not root:
        return True

# 104. Maximum Depth of Binary Tree
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# 107. Binary Tree Level Order Traversal II
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

# 108. Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(nums: list) -> TreeNode:
    n = len(nums)
    if not n:
        return None
    
    mid = n // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    
    return root

# 110. Balanced Binary Tree
def isBalanced(root: TreeNode) -> bool:
    def depth(r):
        if not r:
            return 0
        return 1 + max(depth(r.left), depth(r.right))

    if not root:
        return True
    return abs(depth(root.left) - depth(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)

# 111. Minimum Depth of Binary Tree
def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    minL = minDepth(root.left) if root.left else float("inf")
    minR = minDepth(root.right) if root.right else float("inf")
    return 1 + min(minL, minR)

# 112. Path Sum
def hasPathSum_1(root: TreeNode, sum: int) -> bool:
    def dfs(node):
        if not node:
            return []
        res = dfs(node.left)
        res += dfs(node.right)
        if res:
            return [node.val + i for i in res]
        else:
            return [node.val]
    
    all_sum = dfs(root)
    return sum in all_sum
def hasPathSum_2(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)