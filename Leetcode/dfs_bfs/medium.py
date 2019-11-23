from typing import List

# 200. Number of Islands
def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):   
        grid_extend[i][j] = 0
        if grid_extend[i - 1][j] == "1":
            dfs(i - 1, j)
        if grid_extend[i + 1][j] == "1":
            dfs(i + 1, j)
        if grid_extend[i][j - 1] == "1":
            dfs(i, j - 1)
        if grid_extend[i][j + 1] == "1":
            dfs(i, j + 1) 


    if not grid:
        return 0

    grid_extend, cnt = [[0 for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 2)], 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid_extend[i + 1][j + 1] = grid[i][j]
    
    for i in range(1, len(grid) + 1):
        for j in range(1, len(grid[0]) + 1):
            if grid_extend[i][j] == "1":
                cnt += 1
                dfs(i, j)
    
    return cnt