# 5. Longest Palindromic Substring
def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    max_i, max_j = 0,0
    for i in range(n - 1):
        dp[i][i] = True
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_i, max_j = i, i + 1
    dp[n - 1][n - 1] = True
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            if dp[i + 1][j - 1] and (s[i] == s[j]):
                dp[i][j] = True
                if j - i > max_j - max_i:
                    max_i, max_j = i, j
          
    return s[max_i:max_j + 1]

# 221. Maximal Square
def maximalSquare(self, matrix: List[List[str]]) -> int:
	if len(matrix) == 0:
        return 0

    m, n, curMax = len(matrix), len(matrix[0]), 0
    dp = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        dp[i][0] = 1 if matrix[i][0] == '1' else 0
        curMax = max(curMax, dp[i][0])
    for i in range(n):
        dp[0][i] = 1 if matrix[0][i] == '1' else 0
        curMax = max(curMax, dp[0][i])

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1 if matrix[i][j] == '1' else 0
            curMax = max(curMax, dp[i][j])

    return curMax ** 2