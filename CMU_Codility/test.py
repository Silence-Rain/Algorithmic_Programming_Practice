import math
from functools import cmp_to_key

def arraylistLen(A):
    cur = A[0]
    count = 1
    while cur != -1:
        cur = A[cur]
        count += 1

    return count


def calculateSquare(A, B):
    # Brute force
    # maxi = 0
    # for i in range(A, B + 1):
    # 	count = -1
    # 	cur = float(i)
    # 	while cur.is_integer():
    # 		cur = math.sqrt(cur)
    # 		count += 1

    # 	maxi = count if count > maxi else maxi

    # return maxi

    high = int(math.log2(math.log2(B)))
    bound = [2]
    for i in range(high, 0, -1):
    	temp = B
    	for j in range(i):
    		temp = math.sqrt(temp)
    	bound.append(math.floor(temp))

    for index, item in enumerate(bound[:-1]):
    	ret = high - index + 1
    	for i in range(bound[index], bound[index + 1]):
    		print(ret, i, i ** (2 ** ret))
    		if i ** (2 ** ret) >= A and i ** (2 ** ret) <= B:
    			return ret

    return 0


def battleship(N, S, T):
    ships_raw = [x.split(" ") for x in S.split(",")]
    ships = [[(int(y[0][:-1]) - 1, ord(y[0][-1]) - 65), (int(y[1][:-1]) - 1, ord(y[1][-1]) - 65)] for y in ships_raw]
    ships_cells = [extend_cells(x) for x in ships]
    hits = [(int(y[:-1]) - 1, ord(y[-1]) - 65) for y in T.split(" ")]

    sunk = 0
    hitnotsunk = 0

    for item in ships_cells:
    	ship_len = len(item)
    	hit_cnt = 0
    	for cell in item:
    		if is_hit(hits, cell):
    			hit_cnt += 1

    	if hit_cnt != 0:
    		if hit_cnt == ship_len:
    			sunk += 1
    		else:
    			hitnotsunk += 1

    return "%s,%s" % (sunk, hitnotsunk)
def extend_cells(pos):
	ret = []
	for i in range(pos[0][0], pos[1][0] + 1):
		for j in range(pos[0][1], pos[1][1] + 1):
			ret.append([i, j])

	return ret
def is_hit(hits, pos):
	for item in hits:
		if item[0] == pos[0] and item[1] == pos[1]:
			return True


def baseNegative2Div2(A):
    if len(A) == 0:
    	return []

    total_len = len(A)
    res = [0 for x in range(total_len + 2)]
    # get ceiling
    nums2addup = [] if A[0] == 0 else [[1]]
    # divide by 2
    del A[0]
    for i, item in enumerate(A):
    	if item == 1:
    		temp = [0 for x in range(i)]
    		temp.extend([1,1])
    		nums2addup.append(temp)
    # add them up!
    for item in nums2addup:
    	for j in range(len(item)):
    		temp_add = binary_add(res[j], item[j])
    		res[j] = temp_add[0]
    		if temp_add[1]:
    			if res[j + 1] == 1:
    				res[j + 1] = 0
    			else:
    				res[j + 1] = 1
    				res[j + 2] = 1

    return truncate(res)
# return the result of xor and the increment status
def binary_add(x, y):
	return [x ^ y, True if x == 1 and y == 1 else False]
def truncate(x):
	for i in range(len(x) - 3, 0, -1):
		if x[i] == 1:
			return x[:i + 1]
