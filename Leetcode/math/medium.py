import math

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