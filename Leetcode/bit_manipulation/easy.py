# 136. Single Number
def singleNumber(nums: list) -> int:
    res = 0
    for i in nums:
        res ^= i
        
    return res