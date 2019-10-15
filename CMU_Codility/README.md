## CMU 2019 Codility Test

#### Tests

- **ArrayListLen**

A non-empty array A with length of N represents a linked list. The value of each element represents the index of its next sibling (-1 represents the end of linked list). Calculate the length of linked list. 

- **CalculatetheSquares**

Given 2 integers A and B, find a integer in [A, B], on which we can do maximum square root operations (The result of square root operation should also be an integer). 

- **Battleships**

Given a board with size of N\*N. 

Player A initially put some ships on the board. The ship is a rectangle and occupies at most 4 cells. The positions of ships are given in following format:

`"A1 B2,A3 C3"` (which represents 2 ships. The first ship's upper left cell is A1 and bottom right cell is B2. The second ship's upper left cell is A3 and bottom right cell is C3)

Player B choose some cell to attack. The coordinates are give in following format:

`"A1,A3,B3,C3"` (which means he hits 4 cells, A1, A3, B3 and C3)

Calculate the number of sunk ships and the number of ships which are hit but not sunk. 

*sunk: all cells of a ship are hit*

*hit but not sunk: at least one, but not all cells of a ship are hit*

- **BaseNegative2Div2** 

Let's define a "binary" sequence with the base of -2:

eg. :

| index 0 (-2^0) | index 1 (-2^1) | index 2 (-2^2) | index 3 (-2^3) | index 4 (-2^4) | Decimal integer |
| -------------- | -------------- | -------------- | -------------- | -------------- | --------------- |
| 1              | 0              | 0              | 1              | 1              | 9               |
| 0              | 1              | 1              | 0              | 1              | 18              |

Given a sequence A which represents a decimal integer X, return the shortest sequence which represents ceil(X/2)

