from typing import List

def trap(self, height: List[int]) -> int:
    total = 0
    for i in range(len(height)):
        l, r = 0, 0
        for j in range(0, i + 1):
            l = max(l, height[j])
        for j in range(i, len(height)):
            r = max(r, height[j])
        total += min(l, r) - height[i]
    
    return total