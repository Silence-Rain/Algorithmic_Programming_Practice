# 137. Single Number II
def singleNumber(nums: list) -> int:
    ones, twos = 0, 0
    for i in nums:
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones
    
    return ones