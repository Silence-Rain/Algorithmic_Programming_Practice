from typing import List

# 42. Trapping Rain Water
def trap(height: List[int]) -> int:
	if not height:
        return 0
        
    max_left, max_right, res = [0 for _ in height], [0 for _ in height], 0
    max_left[0], max_right[-1] = height[0], height[-1]
    for i in range(1, len(height)):
        max_left[i] = max(height[i], max_left[i - 1])
        max_right[len(height) - i - 1] = max(height[len(height) - i - 1], max_right[len(height) - i])

    for i in range(len(height)):
        res += min(max_left[i], max_right[i]) - height[i]
        
    return res
    