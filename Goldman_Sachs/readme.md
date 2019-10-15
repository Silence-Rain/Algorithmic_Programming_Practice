# Programming Test of Goldman Sachs's Financial Modelling

### Max Commonality of substrings

**Description:**

Given a string, divide it into two substrings such that the substrings have the most possible characters in common. The *cut commonality* is number of characters in common between the two substrings. Determine the maximum cut commonality.

Determine the maximum cut commonality. For example, given a string, s = " abcdedeara", there are 9 ways of splitting the string into two non-empty substrings. The best possible way is to split it into "abcde" and "deara" which gives the cut commonality of 3 with 1 each for a, d and e.

If a character is repeated, the cut commonality count for that character is the minimum of the count of that character in the two substrings. Given the original string "aabbbbaa", the best split is "aabb" and "bbaa" and the cut commonality is 4 with 2a's and 2b's.

**Sample Test Case:**

- Input: `"abcdecdefg"`

  Output: `3`

- Input: `"zzzxxxzzz"`

  Output: `4`

**Solution:**

Basic idea: Hash table, Python's generator

- Construct a hash table for each substring, initialize it with the frequency of each letter
- Use Python's generator to generate all the possible cut position. To reduce the time complexity, this generator start from the middle of the string, then spread to both left and right
- If the length of one of the substring is less than the largest commonality currently, then return the current largest commonality



### Sort of Shuffled Decimal System

**Description:**

Due to a bug in a trading program, the digits of the decimal system got reshuffled. For instance, each 0 changed to 2, each 1 got changed to 3 and each 2 got changed to 0. If the correct number is "021", the system shows "203". The users of the trading software care about the relative values of their positions. Before rolling out the fix for the underlying issue, the company decided to first issue a modified sorting patch that will show the relative order based on the correct values, sorted ascending.

Given the numbers that the program needs to sort and the mapping, i.e. the shuffled version of the decimal digits, return a list of the jumbled numbers sorted by their correct decimal values, ascending. If multiple mapped values are equal, the values returned should be in the original order they were presented.

For example, `mapping = [3,5,4,6,2,7,9,8,0,1]` of fixed length of `m = 10` and another array of numbers strings, `nums = ['990', '332','32']` of length `n = 3`.

Map '990' as follows:

- The first digit is '9'. In the mapping array, 9 is at position 6 so the first digit of the mapped value is '6'
- The second digit is '9'. Again, the value is at position 6, so the mapped value is now '66'.
- The third digit is '0', found at position 8 of the mapping array. The mapped value is '668' or 668 as an integer.

Map '332' as:

- The first and second digits are both '3' which is found at index 0 in mapping. The mapped value is '00'.
- The third digit is '2' found at index 4 of mapping, so the mapped value is '004' or 4 as an integer. 

The value '32' maps to '04', or integer 4, which equals the previous value.

Ordering by integer values yields `[4, 4, 668]`, and retaining order for '332' and '32' results in a return array of associated original values: `['332', '32', '990']`.

**Sample Test Case:**

- Input: `[2,1,4,8,6,3,0,9,7,5], ["8","12","02","4","023","65","83","224","50"]`

  Output: `['4','224','8','12','83','65','02','50','023']`

**Solution:**

Basic idea: Hash table

- Construct a hash table `dic` from shuffled digit to original digit
- While mapping the shuffled numbers to original numbers, save the corresponding index in a hash table `temp`
- After sorting the original numbers, use the index in `temp` to re-mapping the original numbers into shuffled numbers