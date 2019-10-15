import sys
import numpy as np

class FalseError(Exception):
	def __init__(self, value=""):
		self.value = value


def c1():
	for i, line in enumerate(sys.stdin):
		if i == 0:
			w, h = line.strip().split(",")
			garden = [["B" for _ in range(int(w))] for _ in range(int(h))]
		else:
			t, x, y = line.strip().split(",")
			garden[int(y)][int(x)] = t

	print("\n".join(["".join(item) for item in garden]))


def c2():
	Fs, Ws = [], []
	f_row_map, f_col_map = {}, {}
	for ind, line in enumerate(sys.stdin):
		if ind == 0:
			width, height = [int(x) for x in line.strip().split(",")]
			garden = [["B" for _ in range(width)] for _ in range(height)]
			score = np.array([[0 for _ in range(width)] for _ in range(height)])
		else:
			t, y, x = line.strip().split(",")
			x, y = int(x), int(y)
			garden[x][y] = t
			if t == "F":
				Fs.append((x, y))
			elif t== "W":
				Ws.append((x, y))

	for f in Fs:
		x, y = f
		f_row_map[x] = [y] if x not in f_row_map else f_row_map[x] + [y]
		f_col_map[y] = [x] if y not in f_col_map else f_col_map[y] + [x]
		score[x][y] = -1

		for i in range(width):
			if i != y and score[x][i] != -1:
				score[x][i] += 1
		for i in range(height):
			if i != x and score[i][y] != -1:
				score[i][y] += 1

	for v in f_row_map.values():
		v.sort()
	for v in f_col_map.values():
		v.sort()

	for w in Ws:
		x, y = w
		score[x][y] = -1

		if x in f_row_map:
			cnt_left = 0
			for item in f_row_map[x]:
				if item < y:
					cnt_left += 1
			cnt_right = len(f_row_map[x]) - cnt_left

			for i in range(y):
				if score[x][i] != -1:
					score[x][i] -= cnt_right
			for i in range(y + 1, width):
				if score[x][i] != -1:
					score[x][i] -= cnt_left

		if y in f_col_map:
			cnt_top = 0
			for item in f_col_map[y]:
				if item < x:
					cnt_top += 1
			cnt_bottom = len(f_col_map[y]) - cnt_top

			for i in range(x):
				if score[i][y] != 1:
					score[i][y] -= cnt_bottom
			for i in range(x + 1, height):
				if score[i][y] != 1:
					score[i][y] -= cnt_top

	seats = np.where(score==np.max(score))

	for i in range(len(seats[0])):
		garden[seats[0][i]][seats[1][i]] = "*"

	print("\n".join(["".join(item) for item in garden]))


def c3():
	try:
		stack = []
		for i, line in enumerate(sys.stdin):
			if i == 0:
				width, height = [int(x) for x in line.strip().split(",")]
				garden = [["B" for _ in range(width)] for _ in range(height)]
			elif len(line.strip().split(",")) == 3:
				t, y, x = line.strip().split(",")
				x, y = int(x), int(y)
				garden[x][y] = t
			else:
				op, t, y, x = line.strip().split(",")
				x, y = int(x), int(y)
				
				if op == "Pick up":
					if garden[x][y] != t:
						raise FalseError
					else:
						garden[x][y] = "B"
						stack.append(t)
				elif op == "Plant":
					if garden[x][y] != "B":
						raise FalseError 
					elif stack[-1] != t:
						raise FalseError
					else:
						t1 = stack.pop()
						garden[x][y] = t1

		if stack:
			raise FalseError

	except FalseError:
		print("false\n" + "\n".join(["".join(item) for item in garden]))
		return

	print("true\n" + "\n".join(["".join(item) for item in garden]))  


def c4():

	def man_dist(x, y):
		return abs(x[0]-y[0]) + abs(x[1]-y[1])


	Is, Fs, Ws = [], [], []
	for ind, line in enumerate(sys.stdin):
		if ind == 0:
			width, height = [int(x) for x in line.strip().split(",")]
			garden = [["B" for _ in range(width)] for _ in range(height)]
		else:
			t, y, x = line.strip().split(",")
			x, y = int(x), int(y)
			garden[x][y] = t
			if t == "I":
				Is.append((x, y))
			if t == "F":
				Fs.append((x, y))
			if t == "W":
				Ws.append((x, y))

	score = np.array([[min([man_dist(item, (i,j)) for item in Is]) for j in range(width)] for i in range(height)])

	for w in Ws:
		x, y = w
		score[x][y] = -1

	for w in Ws:
		x, y = w
		#top
		if x - 1 >= 0:
			if score[x - 1][y] > 0:
				dists = []
				if x - 2 >= 0:
					dists.append(score[x - 2][y] + 1)
				if y - 1 >= 0:
					dists.append(score[x - 1][y - 1] + 1)
				if y + 1 < width:
					dists.append(score[x - 1][y + 1] + 1)
				
				cur = min(dists)
				score[x - 1][y] = cur if cur > 0 else -1

		#bottom
		if x + 1 < height:
			if score[x + 1][y] > 0:
				dists = []
				if x + 2 < height:
					dists.append(score[x + 2][y] + 1)
				if y - 1 >= 0:
					dists.append(score[x + 1][y - 1] + 1)
				if y + 1 < width:
					dists.append(score[x + 1][y + 1] + 1)
				
				cur = min(dists)
				score[x + 1][y] = cur if cur > 0 else -1

		#left
		if y - 1 >= 0:
			if score[x][y - 1] >0:
				dists = []
				if y - 2 >= 0:
					dists.append(score[x][y - 2] + 1)
				if x - 1 >= 0:
					dists.append(score[x - 1][y - 1] + 1)
				if x + 1 < height:
					dists.append(score[x + 1][y - 1] + 1)
				
				cur = min(dists)
				score[x][y - 1] = cur if cur > 0 else -1

		#right
		if y + 1 < width:
			if score[x][y + 1]:
				dists = []
				if y + 2 < width:
					dists.append(score[x][y + 2] + 1)
				if x - 1 >= 0:
					dists.append(score[x - 1][y + 1] + 1)
				if x + 1 < height:
					dists.append(score[x + 1][y + 1] + 1)
				
				cur = min(dists)
				score[x][y + 1] = cur if cur > 0 else -1


	F_xs = [i[0] for i in Fs]
	F_ys = [i[1] for i in Fs]
	F_res = score[F_xs, F_ys]

	day = min(F_res)

	for i in range(height):
		for j in range(width):
			if score[i][j] != 0 and score[i][j] != -1 and score[i][j] < day:
				garden[i][j] = "I"

	print(day - 1)
	print("\n".join(["".join(item) for item in garden]))



if __name__ == '__main__':
	c1()
	c2()
	c3()
	c4()
