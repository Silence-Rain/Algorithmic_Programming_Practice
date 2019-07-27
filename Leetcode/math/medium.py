import itertools
import math

# 12. Integer to Roman
def intToRoman(num: int) -> str:
    mapping, digits, ret = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"]
    ], [], []

    while num >= 1:
        digits.append(num % 10)
        num = int(num / 10)
    
    for ind, i in enumerate(digits):
        ret.append(mapping[ind][i])

    ret.reverse()
    
    return "".join(ret)

# 17. Letter Combinations of a Phone Number
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

# 31. Next Permutation
def nextPermutation(self, nums: list) -> None:
    n = len(nums)
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            cur_max = None
            cur_ind = None
            for j in range(i - 1, n):
                if nums[j] > nums[i - 1]:
                    if not cur_max or nums[j] <= cur_max:
                        cur_max = nums[j]
                        cur_ind = j

            temp = nums[i - 1]
            nums[i - 1] = nums[cur_ind]
            nums[cur_ind] = temp

            l = i
            r = n - 1
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp          
                l += 1
                r -= 1
            
            return

    nums.sort()

# 46. Permutations
def permute(nums: list) -> list:
    if len(nums) <= 1:
        return [nums]
    
    res = []
    temp = permute(nums[1:])
    for item in temp:
        for i in range(len(item) + 1):
            res.append(item[:i] + [nums[0]] + item[i:])
    
    return res

# 279. Perfect Squares
def numSquares(n: int) -> int:
    while n % 4 == 0:
        n /= 4

    if n % 8 == 7:
        return 4

    i = 0
    while i ** 2 < n:
        b = int(math.sqrt(n - i ** 2))
        if i ** 2 + b ** 2 == n:
            return 1 if i == 0 else 2

        i += 1

    return 3

# 593. Valid Square
def validSquare(p1: list, p2: list, p3: list, p4: list) -> bool:
    def dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    res = set((dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)))
    return (0 not in res) and len(res) == 2