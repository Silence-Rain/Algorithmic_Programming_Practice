# 1. 2Sum
def twosum(nums: list, target: int) -> list:
    # # Binary search
    # dic = {}
    # for i, item in enumerate(nums):
    #     if item in dic:
    #         dic[item].append(i)
    #     else:
    #         dic[item] = [i]

    # nums.sort()
    # left, right = 0, len(nums) - 1
    # while left < right:
    #     if nums[left] + nums[right] == target:
    #         if nums[left] == nums[right]:
    #             return dic[nums[left]]
    #         else:
    #             return [dic[nums[left]][0], dic[nums[right]][0]]
    #     elif nums[left] + nums[right] < target:
    #         left += 1
    #     else:
    #         right -= 1

    # Hash table
    nums_map = {}
    for ind, i in enumerate(nums):
        if i not in nums_map:
            nums_map[i] = [ind]
        else:
            nums_map[i].append(ind)
    for k, v in nums_map.items():
        if target - k in nums_map:
            if target - k != k:
                return [v[0], nums_map[target - k][0]]
            elif len(nums_map[target - k]) > 1:
                return [v[0], v[1]]

# 26. Remove Duplicates from Sorted Array
def removeDuplicates(nums: list) -> int:
    dup_start, count = 0, 0
    for i in range(len(nums)):
        if nums[dup_start] != nums[i]:
            dup_start = i
            count += 1
            nums[count] = nums[i]
        i += 1

    return count + 1

# 27. Remove Element
def removeElement(nums: list, val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count

# 35. Search Insert Position
def searchInsert(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1 
    if target > nums[-1]:
        return right + 1
    if target < nums[0]:
        return left
    
    while left <= right:
        mid = round((left + right) / 2)
        if nums[mid] == target:
            return mid
        elif mid < len(nums) - 1 and nums[mid] < target <= nums[mid + 1]:
            return mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

# 66. Plus One
def plusOne(digits: list) -> list:
    return [int(i) for i in str(int("".join(map(str, digits))) + 1)]

# 118. Pascal's Triangle
def generate(numRows: int) -> list:
    if not numRows:
        return []

    res = [[1]]
    for i in range(1, numRows):
        temp = [1]
        for j in range(i - 1):
            temp.append(res[i - 1][j] + res[i - 1][j + 1])
        res.append(temp + [1])

    return res

# 119. Pascal's Triangle II
def getRow(rowIndex: int) -> list:
    cur = [1]
    for _ in range(rowIndex):
        res = [1]
        for i in range(len(cur) - 1):
            res.append(cur[i] + cur[i + 1])
        res.append(1)
        cur = res
    
    return cur

# 697. Degree of an Array
def findShortestSubArray(nums: list) -> int:
    m = {}
    for i, item in enumerate(nums):
        if item in m:
            m[item][0] += 1
            m[item][2] = i
        else:
            m[item] = [1, i, i]

    cur = [0, 0, 0]
    for item in m.values():
        if item[0] > cur[0] or (item[0] == cur[0] and item[2] - item[1] < cur[2] - cur[1]):
            cur = item

    return cur[2] - cur[1] + 1