# Solution of Math's problem

### Medium

- \#31 Next Permutation

	Basic idea: The mathematical regularity of next permutation

	- Find first pair of successive elements `nums[i]` and `nums[i - 1]` which satisfies `nums[i] > nums[i - 1]`. Thus, no rearrangement to the right of `nums[i - 1]` can create a larger permutation
	- Find the first larger elements in `[i - 1, n]`, say, `nums[cur_ind]`
	- Swap `nums[cur_ind]` with `nums[i - 1]`
	- Sort `nums[i:]` in ascending order. Since step 1 ensures elements in `[i, n]` are already in descending order, we just need to reverse this part