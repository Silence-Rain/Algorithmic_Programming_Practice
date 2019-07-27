# Solution of Other Problems

### Medium

- \#36 Valid Sudoku

  Basic idea: Hash table, Calculation of coordinates

  - Build up 9 hash tables for each row, column and 3\*3 sub-box to record all the appeared numbers
  - The index of 3\*3 sub-box is `3 * (i // 3) + j // 3`

- \#215 Kth Largest Element in an Array

  Basic idea: Sort

- \#419 Battleships in a Board

  Basic idea: Hash table, Calculation of coordinates

  - Only to find the "first" element of each ship
  - The "first" element is defined as elements that do not have an 'X' to the left and top