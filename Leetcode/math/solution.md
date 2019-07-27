# Solution of Math's Problems

### Easy

- \#7 Reverse Integer

  Basic idea: Transform into a string-process problem

- \#9 Palindrome Number

  Basic idea: Only reverting the first half of `x`, and compare the reverted half with the other half

- \#13 Roman to Integer

  Basic idea: Add the corresponding integer of Roman numerals together according to the rules

- \#69 Sqrt(x)

  Basic idea: Newton's method

### Medium

- \#12 Integer to Roman

  Basic idea: Map

  - Construct a map from integer digit to corresponding Roman numerals, and replace it digit by digit

- \#17 Letter Combinations of a Phone Number

  Basic idea: Descartes Product

  - All possible combinations are actually the Descartes product of the letter sets on all buttons

- \#31 Next Permutation

	Basic idea: The mathematical regularity of next permutation

	- Find first pair of successive elements `nums[i]` and `nums[i - 1]` which satisfies `nums[i] > nums[i - 1]`. Thus, no rearrangement to the right of `nums[i - 1]` can create a larger permutation
	- Find the first larger elements in `[i - 1, n]`, say, `nums[cur_ind]`
	- Swap `nums[cur_ind]` with `nums[i - 1]`
	- Sort `nums[i:]` in ascending order. Since step 1 ensures elements in `[i, n]` are already in descending order, we just need to reverse this part
	
- \#46 Permutations

  Basic idea: Recursive solution

  - Recursively put the current first element into each possible space between all backward elements

- \#279 Perfect Squares

  Basic idea: Lagrange's four-square theorem

  - Since the positive number which satisfies Lagrange's four-square theorem must satisfies this equation: `x = (8b + 7) * 4^a` , we can reduce the complexity by dividing `n` by 4
  - If `n` not satisfies steps above, use brute force to determine whether `n` is a perfect square or it can be expressed as the sum of 2 square numbers
  - Otherwise, return 3

- \#593 Valid Square

  Basic idea: In a valid square, there are only 2 different distances between each pair of vertices