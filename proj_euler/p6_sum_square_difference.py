
def sum_square_diff_bruteforce(limit: int) -> int:
	sum_of_squares = 0
	square_of_sum = 0
	for i in range(1, limit + 1):
		sum_of_squares += i**2
		square_of_sum += i
	square_of_sum = square_of_sum**2

	print(f'Sum of Squares: {sum_of_squares}, Square of Sum: {square_of_sum}')
	return square_of_sum - sum_of_squares

def sum_square_diff_triangular(limit: int) -> int:
	sum_of_squares = 0
	for i in range(1, limit + 1):
		sum_of_squares += i**2
	square_of_sum = (limit * (limit + 1) // 2)**2
	return square_of_sum - sum_of_squares

# derive equation for sum_of_squares


if __name__ == '__main__':
	limit = 10000000
	# limit = 10
	# print(f'Difference: {sum_square_diff_bruteforce(limit)}') 		# ~4.6 sec w limit = 10 mil
	print(f'dif 2: {sum_square_diff_triangular(limit)}')				# ~ 4.3 sec