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