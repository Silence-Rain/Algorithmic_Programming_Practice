#  olution of Dynamic Programming's Problems

### Easy

- \#53 Maximum Subarray

  - Construct a matrix `dp` to remember the maximum subarray ending with index `i` .
  - Starting from index 0, update the value of the current element as `dp[i] = max(dp[i-1] + nums[i], nums[i])` 
  

### Medium

- \#221 Maximal Square

  - Construct a matrix `dp` to remember the largest square so far. `dp[i][j]` represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix
  - Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as `dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1`  
