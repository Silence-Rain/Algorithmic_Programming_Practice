# 36. Valid Sudoku
def isValidSudoku(board: list) -> bool:
    rows = [{} for i in range(9)]
    cols = [{} for i in range(9)]
    boxes = [{} for i in range(9)]
    
    for i in range(9):
        for j in range(9):
            elem = board[i][j]
            if elem != ".":
                if elem in rows[i] or elem in cols[j] or elem in boxes[3 * (i // 3) + j // 3]:
                    return False
                else:
                    rows[i][elem] = 1
                    cols[j][elem] = 1
                    boxes[3 * (i // 3) + j // 3][elem] = 1
    
    return True

# 215. Kth Largest Element in an Array
def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

# 419. Battleships in a Board
def battleship(board):
    if len(board) == 0:
        return 0

    row_len, col_len, count = len(board), len(board[0]), 0
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                count += 1

    return count 