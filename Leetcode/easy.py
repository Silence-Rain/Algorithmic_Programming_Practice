def twosum(nums, target):
    dic = {}
    for i, item in enumerate(nums):
        if item in dic:
            dic[item].append(i)
        else:
            dic[item] = [i]

    nums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            if nums[i] == nums[j]:
                return dic[nums[i]]
            else:
                return [dic[nums[i]][0], dic[nums[j]][0]]


        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

def reverse(x: int) -> int:
    xlist = list(str(x))
    xlist.reverse()
    
    if xlist[-1] == '-':
        xlist.pop()
        xlist.insert(0, '-')
        
    ret = int("".join(xlist))
    return ret if ret >= - 2 ** 31 and ret <= 2 ** 31 - 1 else 0

def isPalindrome_simple(x: int) -> bool:
    s = str(x)
    rev = str(x)[::-1]
    return s == rev

def isPalindrome_no_str(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x = int(x / 10)
        
    return x == reverted or x == int(reverted / 10)

def longestCommonPrefix(strs: List[str]) -> str:
    ind = 0
    n = len(strs)
    
    if n == 0:
        return ""
    elif n == 1:
        return strs[0]
    else:
        try:
            while True:
                for i in range(1, n):
                    if strs[i - 1][ind] != strs[i][ind]:
                        return strs[0][:ind]
                ind += 1
        except:
            return strs[0][:ind]

def remove_duplicates(nums):
    i = 0
    j = 0
    count = 0

    while j < len(nums):
        if nums[i] != nums[j]:
            i = j
            count += 1
            nums[count] = nums[i]
        j += 1

    return count + 1

def findShortestSubArray(nums):
    m = {}
    for i,item in enumerate(nums):
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