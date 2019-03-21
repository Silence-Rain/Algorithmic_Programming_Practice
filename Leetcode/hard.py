import math

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    res = []
    flag = (m + n) % 2 == 1
    cnt = math.ceil((m + n) / 2) if flag else int((m + n) / 2 + 1)
    
    for i in range(0, cnt):
        if len(nums1) == 0:
            res.append(nums2.pop(0))
        elif len(nums2) == 0:
            res.append(nums1.pop(0))
        else:
            if nums1[0] >= nums2[0]:
                res.append(nums2.pop(0))
            else:
                res.append(nums1.pop(0))

    return float(res[-1]) if flag else (res[-2] + res[-1]) / 2.0
