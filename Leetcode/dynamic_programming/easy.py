import math
from typing import List

# 53. Maximum Subarray
def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return -math.inf

    n, cur_max, dp = len(nums), nums[0], [nums[0]]
    for i in range(1, n): 
        dp.append(max(dp[i - 1] + nums[i], nums[i]))

    return max(dp)  