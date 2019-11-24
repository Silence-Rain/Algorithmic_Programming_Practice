# Solution of Array's Problems

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

- \#66 Plus One

  Basic idea: `List.map()`, list comprehensions

- \#118 Pascal's Triangle

  Basic idea: Simple iterative solution

- \#119 Pascal's Triangle II

  Basic idea: Simple iterative solution, only need to save last row

- \#697 Degree of an Array

  Basic idea: Hash table

  - Traverse the array. Calculate each element's frequency, start index, and end index, then save into a hash table
  - Traverse the hash table, find the most frequent element, return the distance between its start index and end index

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

- \#59 Spiral Matrix II

  Basic idea: Generator

  - Use Python's feature: iterator & generator, produce the next coordinate in order

- \#74 Search a 2D Matrix

  Basic idea: Binary search

  - Perform 2 binary search. Pinpoint  `targetRow` in the first time, then find the target element

- \#75 Sort Colors

  Basic idea: 2 pointers & partition

  - Since there are only 3 types of elements, after sort, '0' must be placed at the left side, '1' must be placed at the middle, and '2' must be placed at the right side
  - Maintain 2 pointers: `l` represents the end of '0' area, `r` represents the beginning of '2' area
  - If current element is '0', swap it with `nums[l]`. If it is '2', swap it with `nums[r]`. Otherwise, do nothing

- \#238 Product of Array Except Self

  - The expected result is actually `totalProduct / currentValue`
  - Consider the affect of 0

- \#525 Contiguous Array

  Basic idea: Hash map

  - Construct a hash map in which key represents how much more 1s than 0s, and value represents the index
  - When the `key` is `0`, it shows that we've encountered equal number of 0s and 1s from the beginning till the current index
  - If we encounter the same `key` twice while traversing the array, it means that the number of 0s and 1s are equal between the indices corresponding to the equal `key` values.

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