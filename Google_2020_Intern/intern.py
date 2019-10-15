def maximum_time(t):
	res = ['', '', ':', '', '']
	res[0] = t[0] if t[0] != '?' else ('1' if t[1] != '?' and t[1] > '3' else '2')
	res[1] = t[1] if t[1] != '?' else ('9' if t[0] != '?' and t[0] <= '1' else '3')
	res[3] = t[3] if t[3] != '?' else '5'
	res[4] = t[4] if t[4] != '?' else '9'
	
	return ''.join(res)

def compare_string(A, B):
	As, Bs = A.split(","), B.split(",")
	A_stats = [i.count(min(i)) for i in As]
	B_stats = [i.count(min(i)) for i in Bs]

	return [sum([(1 if b > a else 0) for a in A_stats]) for b in B_stats]

def largest_subarray(A, k):
	start = 0
	for i in range(1, len(A) - k + 1):
		for j in range(k):
			if A[start + j] < A[i + j]:
				start = i
				break
			elif A[start + j] > A[i + j]:
				break

	return A[start:start+k]


if __name__ == '__main__':
	print(largest_subarray([1,4,4,3,2,5], 3))