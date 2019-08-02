def maxCommon(s):
	def indexGenerator(n):
		start = n // 2
		yield start
		for i in range(1, start):
			yield start + i
			yield start - i
		if n % 2:
			yield n - 1

	n, res = len(s), 0
	for i in indexGenerator(n):
		dic1, dic2, curMax = {}, {}, 0
		for c in s[:i]:
			dic1[c] = dic1[c] + 1 if c in dic1 else 1
		for c in s[i:]:
			dic2[c] = dic2[c] + 1 if c in dic2 else 1

		for k, v in dic1.items():
			if k in dic2:
				curMax += min(v, dic2[k])

		res = max(curMax, res)
		if i < res or n - i < res:
			break

	return res

def strangeSort(mapping, nums):
	dic, temp = {}, {}
	for ind, i in enumerate(mapping):
		dic[str(i)] = str(ind)

	for ind, i in enumerate(nums):
		temp[ind] = int("".join([dic[j] for j in i]))

	res = [nums[i[0]] for i in sorted(temp.items(), key=lambda x:x[1])]
	return res


if __name__ == '__main__':
	print(strangeSort([2,1,4,8,6,3,0,9,7,5], ["8","12","02","4","023","65","83","224","50"]))
	# print(maxCommon("abcdedeara"))