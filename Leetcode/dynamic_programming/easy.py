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

# 121. Best Time to Buy and Sell Stock
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
        
    n, cur_max = len(prices), 0
    prev_min, after_max = [0] * n, [0] * n
    prev_min[0], after_max[-1] = prices[0], prices[-1]
    for i in range(1, n):
        prev_min[i] = min(prices[i], prev_min[i - 1])
    for i in range(n - 2, -1, -1):
        after_max[i] = max(prices[i], after_max[i + 1])
    for i in range(1, n):
        cur_max = max(cur_max, after_max[i] - prev_min[i])
        
    return cur_max