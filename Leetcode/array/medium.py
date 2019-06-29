# 11. Container With Most Water
def maxArea(height: list) -> int:
    left, right, maxArea = 0, len(height) - 1, 0
    while left != right:
        if height[left] < height[right]:
            minHeight = height[left]
            left += 1
        else:
            minHeight = height[right]
            right -= 1
        
        maxArea = max(maxArea, (right - left + 1) * minHeight)

# 15. 3Sum
def threeSum(nums: list) -> list:
    nums.sort()
    n, res = len(nums), []
    if n == 0 or nums[0] > 0 or nums[n - 1] < 0:
        return []
    for k in range(n):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        target = 0 - nums[k]

        i = k + 1
        j = n - 1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[k], nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

    return res

# 33. Search in Rotated Sorted Array
def search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = round((left + right) / 2)
        if nums[mid] == target:
            return mid     
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# 34. Find First and Last Position of Element in Sorted Array
def searchRange(nums: list, target: int) -> list:
    left, right, res = 0, len(nums) - 1, [-1, -1]
    while left <= right:
        mid = round((left + right) / 2)
        if nums[mid] == target:
            cur_l = cur_r = mid
            while cur_l > 0 and nums[cur_l - 1] == target:
                cur_l -= 1
            while cur_r < len(nums) - 1 and nums[cur_r + 1] == target:
                cur_r += 1
            res = [cur_l, cur_r]
            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return res

# 48. Rotate Image
def rotate_1(matrix: list) -> None:
    n = len(matrix)
    for i in range(math.ceil(n/2)):
        for j in range(math.floor(n/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i] 
            matrix[j][n - 1 - i] = temp
def rotate_2(matrix: list) -> None:
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

# 54. Spiral Matrix
def spiralOrder(matrix: list) -> list:
    if not matrix:
        return []

    m, n, ret = len(matrix), len(matrix[0]), []
    cnt = min(m, n) // 2 + 1 if min(m, n) % 2 else min(m, n) // 2
    for i in range(cnt):
        ret.extend(matrix[i][i:n - i])
        for j in range(i + 1, m - i):
            ret.append(matrix[j][n - i - 1])
        if i + 1 != m - i and i + 1 != n - i:
            ret.extend(matrix[m - i - 1][i:n - i - 1][::-1])
            for j in range(m - i - 2, i, -1):
                ret.append(matrix[j][i])

    return ret

# 56. Merge Intervals