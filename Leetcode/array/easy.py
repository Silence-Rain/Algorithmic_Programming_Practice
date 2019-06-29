# 1. 2Sum
def twosum(nums: list, target: int) -> list:
    dic = {}
    for i, item in enumerate(nums):
        if item in dic:
            dic[item].append(i)
        else:
            dic[item] = [i]

    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            if nums[left] == nums[right]:
                return dic[nums[left]]
            else:
                return [dic[nums[left]][0], dic[nums[right]][0]]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

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