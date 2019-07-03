class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 145. Binary Tree Postorder Traversal
def postorderTraversal(root: TreeNode) -> list:
    if not root:
        return []
    
    res = self.postorderTraversal(root.left)
    res += self.postorderTraversal(root.right)
    res.append(root.val)
    
    return res