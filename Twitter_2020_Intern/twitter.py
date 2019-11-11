import math
from collections import Counter

def balancedSum(sales):
    total, l = sum(sales), 0
    for i in range(len(sales)):
        total -= sales[i]
        if l == total:
            return i
        l += sales[i]

def finalInstances(instances, averageUtil):
    if not averageUtil:
        return instances
    i = 0
    while i < len(averageUtil):
        if averageUtil[i] > 60 and instances < 10 ** 8:
            instances *= 2
            i += 10
        elif averageUtil[i] < 25 and instances > 1:
            instances = math.ceil(instances / 2)
            i += 10
        i += 1

    return instances

def fountainActivation(a):
    ranges, ret = [0] * len(a), 1
    for i in range(len(a)):
        l = max(i - a[i], 0)
        r = min(i + a[i] + 1, len(a))
        ranges[l] = max(ranges[l], r)
    
    cur, next = ranges[0], 0
    for i in range(len(a)):
        next = max(next, ranges[i])
        if i == cur:
            ret += 1
            cur = next

    return ret


def getUniqueUserIdSum(arr):
    total = 0
    cnts = Counter(arr)

    for i in range(len(arr)):
        if cnts[arr[i]] > 1:
            temp = arr[i] + 1
            while temp in cnts:
                temp += 1

            total += temp
            cnts[temp] = 1
            cnts[arr[i]] -= 1

            arr[i] = temp

        else:
            total += i

    return total

if __name__ == '__main__':
    finalInstances()