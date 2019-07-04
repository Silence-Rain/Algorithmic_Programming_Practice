# Solution of Linked List's problem

### Easy

- \#21 Merge Two Sorted Lists

  Basic idea: Merge sort - the merge part

- \#83 Remove Duplicates from Sorted List

  Basic idea: 2 pointers

  - Set a fast pointer `p` which moves one step faster than `last`
  - If `p.val == last.val`, move `p` forward to skip duplicate element

- \#206 Reverse Linked List

  Basic idea: Dummy node

  - Start with the first element `head`, remove its next element and insert it after the dummy node

### Medium

- \#2 Add Two Numbers

  Basic idea: Binary full-adder

- \#19 Remove Nth Node From End of List

  Basic idea: 2 pointers

- \#24 Swap Nodes in Pairs

  Basic idea: Dummy node

  - Simplified version of #25

- \#61 Rotate List

  Basic idea: 2 pointers

  - Traverse the list, get the total length `n`
  - Calculate the actual rotate steps `diff`
  - Set a fast pointer `p` to move `n - diff - 1` steps in advance, then `p` is the first element of the returned list
  - Concat the first half of the given list to the end of `p`

- \#82 Remove Duplicates from Sorted List II

  Basic idea: 2 pointers, set

  - Similar to #83, set 2 pointer to skip all the duplicate elements while saving the duplicate value into a set
  - Traverse the list again, remove all the node whose value is in the set

- \#92 Reverse Linked List II

  Basic idea: Dummy node

  - Similar to #206. Regard the node before `m` as the dummy node, and the node `n` as the end of the list

- \#109 Convert Sorted List to Binary Search Tree

  Basic idea: 2 pointers

  - Typical recursive construction method of BST, similar to #108
  - Set a fast pointer which moves twice fast as the slow one, thus find the middle point of the list

### Hard

- \#23 Merge k Sorted Lists

  Basic idea: Merge sort - the merge part

- \#25 Reverse Nodes in k-Group

  Basic idea: Dummy node

  - Regard every node before a k-group as the dummy node of this k-group, then the "reverse" action can be transformed into "remove at tail then insert to head" operation