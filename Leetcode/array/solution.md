# Solution of Array's Problem

### Easy

- \#1 2Sum

  Basic idea: 2 pointers, hash table

  - Construct a hash table from value of array element to its index(s)
  - Sort the array in ascending order
  - Set up 2 pointers: `left` at the head and `right` at the tail of array
  - If `nums[left] + nums[right] == target`, return the index of `nums[left]` and `nums[right]` from the hash table
  - If `nums[left] + nums[right] > target`, decrease `right`. Otherwise increase `left`

- \#26 Remove Duplicates from Sorted Array

  Basic idea: 2 pointers

  - Set up 2 pointers: `dup_start` represents the beginning of the continuous duplicates, `count` represents the amount of distinct elements
  - Traverse the array. If current element's value does not equal to the value of `nums[dup_start]`, increase `count` by 1, set `dup_start` to current index, and copy current element's value to  `nums[count]` 

- \#27 Remove Element

  Basic idea: 2 pointers. Similar to #26

- \#35 Search Insert Position

  Basic idea: Binary search

  - When `nums[mid] < target <= nums[mid + 1]`, we can determine the proper insert position to be `mid + 1`

### Medium

- \#11 Container With Most Water

  Basic idea: 2 pointers

  - Set up 2 pointers: `left` at the head and `right` at the tail of array
  - Before `left` meets `right`, calculate current area formed by them, and update `maxArea` by taking the greater one between current area and previous value of `maxArea`

- \#15 3Sum

  Basic idea: 2 pointers

  - Sort the array in ascending order
  - Handle the corner cases
  - Successively select the `k`th element in `nums`, then reduce the problem into `twosum(nums[k+1:], -nums[k])`

- \#33 Search in Rotated Sorted Array

  Basic idea: Binary search

  - Similar to a simple binary search. The difference is the method to determine `left` or `right` need to be assigned
  - When `nums[left] <= nums[mid]`, it means the rotated pivot is in the right half. Thus, it is a simple binary search, and vice versa

- \#34 Find First and Last Position of Element in Sorted Array

  Basic idea: Binary search

  - Use binary search to pinpoint the `target` value, then use linear scan to find the left and right boundary

- \#48 Rotate Image

  Basic idea: Brute force / Use a little bit sense of symmetry

  Brute force:

  - Calculate the destination coordinate of each element and rotate them in order

  Symmetry:

  - Rotate 90 degree clockwise => reverse the array, then perform an axial symmetry by the diagonal

- \#54 Spiral Matrix

  Basic idea: "Traverse" the matrix by layers

  - Calculate `cnt` as the number of layers
  - For each layer, calculate the path of coordinates

- \#56 Merge Intervals

  Basic idea: Sort and traverse

  - Sort the array by the left boundary of intervals
  - Traverse the array. If current interval's left boundary is less than the right boundary of previous interval, then we can merge them 

### Hard

- \#4 Median of Two Sorted Arrays

  Basic idea: Merge sort - the "Merge" part

  - Calculate the position of median `pos`. (2 scenarios: Odd or even)
  - Iteratively pop exactly `pos` elements from the head of both arrays, and save the latest element to variable `temp`
  - In odd scenario, the final value of `temp` is the median itself
  - In even scenario, the median is the average of the final value and the next potential value of `temp`

- \#41 First Missing Positive

  Basic idea: The first missing positive must be in the range of `[1, n + 1]`

  - Construct an array `flags`, representing the appearance of `[1, n + 1]`
  - Traverse the array. If current element is greater than n, skip it. Otherwise, set the corresponding item of `flags` to be `True`
  - Traverse `flags`, find the first `False` and return its index

- \#57 Insert Interval

  Basic idea: Since given intervals are non-overlapping, we can transform "insertion" into "concatenation"

  - For each interval, if its right boundary is less than the left boundary of `newInterval`, it should be placed at the left side of `newInterval`, and vice versa
  - Concat the intervals which should be placed at the left side, `newInterval`, and the intervals which should be placed at the right side
