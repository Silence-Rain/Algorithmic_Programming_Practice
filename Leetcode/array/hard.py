# 4. Median of Two Sorted Arrays
def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    m, n, temp = len(nums1), len(nums2), -1
    flag = (m + n) % 2 == 1
    pos = math.ceil((m + n) / 2) if flag else int((m + n) / 2)

    for i in range(0, pos):
        if not nums1:
            temp = nums2.pop(0)
        elif not nums2:
            temp = nums1.pop(0)
        elif nums1[0] >= nums2[0]:
            temp = nums2.pop(0)
        else:
            temp = nums1.pop(0)
    
    if flag:
        return float(temp)
    else:
        if not nums1:
            return (temp + nums2[0]) / 2.0
        elif not nums2:
            return (temp + nums1[0]) / 2.0
        else:
            return (temp + min(nums1[0], nums2[0])) / 2.0

# 41. First Missing Positive
def firstMissingPositive(nums: list) -> int:
    n = len(nums)
    flags = [False for _ in range(n + 1)]
    for i in range(n):
        if nums[i] > n:
            continue
        if nums[i] > 0:
            flags[nums[i] - 1] = True
            
    for i in range(len(flags)):
        if flags[i] == False:
            return i + 1

# 57. Insert Interval
def insert(intervals: list, newInterval: list) -> list:
    left, right = [], []
    start, end = newInterval[0], newInterval[1]
    
    for i in intervals:
        if i[1] < start:
            left.append(i)
        elif i[0] > end:
            right.append(i)
        else:
            start = min(i[0], start)
            end = max(i[1], end)
    
    return left + [[start, end]] + right