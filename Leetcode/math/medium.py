# 31. Next Permutation
def nextPermutation(self, nums: List[int]) -> None:
    n = len(nums)
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            cur_max = None
            cur_ind = None
            for j in range(i - 1, n):
                if nums[j] > nums[i - 1]:
                    if not cur_max or nums[j] <= cur_max:
                        cur_max = nums[j]
                        cur_ind = j

            temp = nums[i - 1]
            nums[i - 1] = nums[cur_ind]
            nums[cur_ind] = temp

            l = i
            r = n - 1
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp          
                l += 1
                r -= 1
            
            return

    nums.sort()