# Solution of Tree's Problem

### Easy

- \#100 Same Tree

  Basic idea: Recursive solution

  - Two trees are same iff their left subtree and right subtree are both the same

- \#101 Symmetric Tree

  Basic idea: Recursive solution

  - Two trees are symmetrical iff their values are the same, and one's left subtree is symmetrical with the other's right subtree and vice versa

- \#104 Maximum Depth of Binary Tree

  Basic idea: Recursive solution

  - The maximum depth of a binary tree is 1 plus the maximum depth between its left and right subtrees

- \#107 Binary Tree Level Order Traversal II

  Basic idea: Exactly the same as #102

- \#108 Convert Sorted Array to Binary Search Tree

  Basic idea: Definition of BST

- \#110 Balanced Binary Tree

  Basic idea: Recursive solution

  - A binary tree is balanced iff its left and right subtrees are both balanced, and the height difference is not greater than 1

- \#111 Minimum Depth of Binary Tree

  Basic idea: Recursive solution

  - The minimum depth of a binary tree is the minimum depth between its left and right subtrees
  - If one of its subtrees is empty, the minimum depth is the depth of the other subtree

- \#112 Path Sum

  Basic idea: DFS / Recursive solution

  DFS:

  - Traverse all the possible paths, calculate the sum along the path

  Recursive: 

  - If current node's value equals to `sum`, return `True`
  - Otherwise, find if there is a path along which the sum is `sum` - current node's value

### Medium

- \#94 Binary Tree Inorder Traversal

  Basic idea: Recursive solution

- \#102 Binary Tree Level Order Traversal

  Basic idea: BFS using queue

  - Add  `level` to help integrating nodes in the same level

- \#103 Binary Tree Zigzag Level Order Traversal

  Basic idea: BFS using deque

  - Add `flag` to help determining the direction
  - When nodes in the same one level are all popped, nodes still in deque are exactly all nodes in the next level

- \#105 Construct Binary Tree from Preorder and Inorder Traversal

  Basic idea: Recursive construction method

  - Current `root` node must be the first element of `preorder`
  - Find the `root` node in `inorder`, then the left side of `root` is its left subtree, and vice versa

- \#106 Construct Binary Tree from Inorder and Postorder Traversal

  Basic idea: Recursive construction method

  - Current `root` node must be the last element of `postorder`
  - Find the `root` node in `inorder`, then the left side of `root` is its left subtree, and vice versa

- \#113 Path Sum II

  Basic idea: Recursive DFS

- \#116 Populating Next Right Pointers in Each Node

  Basic idea: BFS

  - Since the given tree is a perfect binary tree, then assuming current node is `cur`, we have:
    - `cur.left.next` is `cur.right`
    - `cur.right.next` is `cur.next.left`

- \#117 Populating Next Right Pointers in Each Node II

  Basic idea: BFS

  - Similar to #116, but the given tree is not perfect. So we need to remember the `head` and `tail` of next level
  - When current level is finished, move the pointer to `head` to start traverse the next level

- \#129 Sum Root to Leaf Numbers

  Basic idea: Recursive DFS

- \#144 Binary Tree Preorder Traversal

  Basic idea: Recursive solution

### Hard

- \#145 Binary Tree Postorder Traversal

  Basic idea: Recursive solution