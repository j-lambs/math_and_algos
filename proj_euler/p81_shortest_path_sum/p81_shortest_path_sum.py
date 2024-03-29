
# 2427 for 5x5 file
if __name__ == '__main__':
	file = open("005.txt", "r")
	for line in file:
		line = line.rstrip("\n")

		print(line)


	file.close()