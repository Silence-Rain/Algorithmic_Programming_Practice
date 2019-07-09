import math
import re
import itertools

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    
    mat = [[] for _ in range(numRows)]
    n = len(s)
    for i in range(n):
        size = 2 * (numRows - 1)
        tempInd = i % size
        index = tempInd if tempInd < size / 2 else size - tempInd
        mat[index].append(s[i])
        
    return "".join(["".join(x) for x in mat])

def myAtoi(str: str) -> int:
    match = re.match(r'^(\s*[\+\-]?[0-9]+)[^0-9]+', str)
    INT_MAX = 2 ** 31 - 1
    INT_MIN = - 2 ** 31

    try:
        if match:
            ret = int(match.group(1))
        else:
            ret = int(str)
    except ValueError as e:
        ret = 0

    return INT_MAX if ret > INT_MAX else (ret if ret >= INT_MIN else INT_MIN)

def intToRoman(num: int) -> str:
    mapping = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"]
    ]
    digits = []
    ret = []

    while num >= 1:
        digits.append(num % 10)
        num = int(num / 10)
    
    for ind, i in enumerate(digits):
        print(ind, i)
        ret.append(mapping[ind][i])

    ret.reverse()
    
    return "".join(ret)

def romanToInt(s: str) -> int:
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ret = 0
    n = len(s)
    
    for i in range(n - 1):
        cur = mapping[s[i]]
        next = mapping[s[i + 1]]
        if cur >= next:
            ret += cur
        else:
            ret -= cur
            
    return ret + mapping[s[n - 1]]

def letterCombinations(digits: str):
    if len(digits) == 0:
        return []
    
    maps = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    arr = [maps[x] for x in list(digits)]
    return ["".join(x) for x in itertools.product(*arr)]

def generateParenthesis(n: int) -> list:
    ret = []
    
    def enum(s, lcnt = 0, rcnt = 0):
        if len(s) == 2 * n:
            ret.append(s)
            return
        if lcnt < n:
            enum(s + '(', lcnt + 1, rcnt)
        if rcnt < lcnt:
            enum(s + ')', lcnt, rcnt + 1)

    enum("")
    return ret

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

def permute(nums: list) -> list:
    if len(nums) <= 1:
        return [nums]
    
    res = []
    temp = self.permute(nums[1:])
    for item in temp:
        for i in range(len(item) + 1):
            res.append(item[:i] + [nums[0]] + item[i:])
    
    return res

def simplifyPath(path: str) -> str:
    dirs = path.split('/')
    stack = []
    for i in range(1, len(dirs)):
        if dirs[i] == ".." and len(stack):
            stack.pop()
        elif not len(dirs[i]) or dirs[i] == "." or (dirs[i] == ".." and not len(stack)):
            pass
        else:
            stack.append(dirs[i])

    return "/" + "/".join(stack)

def singleNumber(nums: list) -> int:
    ones, twos = 0, 0
    for i in nums:
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones
    
    return ones

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

def battleship(board):
    if len(board) == 0:
        return 0

    row_len = len(board)
    col_len = len(board[0])
    count = 0

    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                count += 1

    return count

def findMaxLength(nums):
    key = 0
    maxi = 0
    m = {0: -1}

    for i in range(len(nums)):
        key += -1 if nums[i] == 0 else 1
        if key in m:
            maxi = maxi if maxi > i - m[key] else i - m[key]
        else:
            m[key] = i

    return maxi

