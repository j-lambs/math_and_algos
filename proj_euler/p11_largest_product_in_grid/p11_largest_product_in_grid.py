"""
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the grid?
"""

"""
Dont have a beautiful or efficient soln, but it breaks each problem down into simple parts
"""

N = 4
# N = 3

def max_prods_vertical(n: int, matrix: [[]]) -> int:
	max_prod_vert = 0
	max_multipliers = []

	# j traverses cols
	for j in range(len(matrix)):
		# i traverses rows
		for i in range(len(matrix[0]) - N + 1):
			t = 1		# is product of current iteration going down
			list_multipliers = []
			# only traverse num adjacent entries that we want
			# also do not go out of bounds of matrix
			for c in range(N):
				multiplier = matrix[i + c][j]
				list_multipliers.append(multiplier)
				t *= multiplier
			# update max_prod and max_multipliers
			if t > max_prod_vert:
				max_prod_vert = t
				max_multipliers = list_multipliers
	print(f'Multipliers of Max Vertical Product: {max_multipliers}')
	return max_prod_vert

def max_prods_horizontal(N: int, matrix: [[]]) -> int:
	max_prod_horiz = 0
	max_multipliers = []

	# i traverses rows
	for i in range(len(matrix)):
		# j traverses cols
		for j in range(len(matrix[0]) - N + 1):
			t = 1		# is product of current iteration going down
			list_multipliers = []
			# only traverse num adjacent entries that we want
			# also do not go out of bounds of matrix
			for c in range(N):
				multiplier = matrix[i][j + c]
				list_multipliers.append(multiplier)
				t *= multiplier
			# update max_prod and max_multipliers
			if t > max_prod_horiz:
				max_prod_horiz = t
				max_multipliers = list_multipliers
	print(f'Multipliers of Max Horizontal Product: {max_multipliers}')
	return max_prod_horiz

# Go down rows first
# You need to check diag down AND diag up (and to the right)
# 8*37*31 = 9176
def max_prods_diagonal(N: int, matrix: [[]]):
	downright = max_prods_diag_downright(N, matrix)
	upright = max_prods_diag_upright(N, matrix)
	bigger = max(downright[0], upright[0])
	return bigger
	# x = bigger[0]
	# print(f'hello {x}')
	# print(f'Multipliers of Max Diagonal Product: {bigger[1]}')
	# return bigger[0]

def max_prods_diag_downright(N: int, matrix: [[]]):
	max_prod_diag = 0
	max_multipliers = []

	# i traverses rows (down)
	for i in range(len(matrix) - N + 1):
		# j traverses cols (horiz)
		for j in range(len(matrix[0]) - N + 1):
			t = 1  # is product of current iteration going down
			list_multipliers = []
			# only traverse num adjacent entries that we want
			# also do not go out of bounds of matrix
			for c in range(N):
				multiplier = matrix[i + c][j + c]
				list_multipliers.append(multiplier)
				t *= multiplier
			# update max_prod and max_multipliers
			if t > max_prod_diag:
				max_prod_diag = t
				max_multipliers = list_multipliers
	# print(f'Multipliers of Max Diagonal Product: {max_multipliers}')
	return (max_prod_diag, max_multipliers)

def max_prods_diag_upright(N: int, matrix: [[]]):
	max_prod_diag = 0
	max_multipliers = []

	# i traverses rows (down)
	for i in range(len(matrix) - 1, N - 2, -1):
		# j traverses cols (horiz)
		for j in range(len(matrix[0]) - N + 1):
			t = 1  # is product of current iteration going down
			list_multipliers = []
			# only traverse num adjacent entries that we want
			# also do not go out of bounds of matrix
			for c in range(N):
				multiplier = matrix[i - c][j + c]
				list_multipliers.append(multiplier)
				t *= multiplier
			# update max_prod and max_multipliers
			if t > max_prod_diag:
				max_prod_diag = t
				max_multipliers = list_multipliers
	# print(f'Multipliers of Max Diagonal Product: {max_multipliers}')
	return (max_prod_diag, max_multipliers)

if __name__ == '__main__':
	# file = open("20x20_grid.txt", "r")
	file = open("20x20_grid.txt", "r")

	grid = [] 	# will be a 2D Array, a matrix containing our ints from txt file '20x20_grid.txt'
	for line in file:
		# Pythonic! Get rid of last char in string (which is \n)
		if line[:-1] == ' ':
			line = line[:-1]
		line = line.split(" ")	# line: continuous string -> array w strings split at each " "
		line = [int(i) for i in line] 	# List Comp: cast each str in line to int
		grid.append(line)


	print(f'Max Prod Vert: {max_prods_vertical(N, grid)}')
	print(f'Max Prod Horiz: {max_prods_horizontal(N, grid)}')
	print(f'Max Prod Diag: {max_prods_diagonal(N, grid)}')
	vert = max_prods_vertical(N, grid)
	horiz = max_prods_horizontal(N, grid)
	diag = max_prods_diagonal(N, grid)

	print(f'Max product of N adjacent entries in matrix: {max(vert, horiz, diag)}')

	file.close()
