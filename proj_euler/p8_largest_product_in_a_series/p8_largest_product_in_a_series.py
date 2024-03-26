
def get_product_of_list(myList: list) -> int:
    product = 1
    for x in myList:
        product *= x
    return product

# kinda slow, there must be a way to read and find max_product in same loop
if __name__ == '__main__':
    num_adjacent_digits = 13

    file = open("large_int.txt", "r")
    list_digits = []
    # read file that holds large int line by line
    for line in file:
        line = line.rstrip("\n")    # strip newline at end of each line
        # put each digit into list_digits as ints
        for ch in line:
            list_digits.append(int(ch))
    file.close()

    # 2 pointer technique, p1 = start of adjacent product range, p2 = end of adj prod range
    # get product of each "window"
    p1 = 0
    p2 = num_adjacent_digits - 1
    max_product = get_product_of_list(list_digits[p1:p2 + 1])
    max_product_range = (p1, p2)
    while p2 < len(list_digits):
        cur_product = get_product_of_list(list_digits[p1:p2 + 1])
        if cur_product > max_product:
            max_product = cur_product
            max_product_range = (p1, p2)
        p1 += 1
        p2 += 1

    print(f'Max Product: {max_product}')

    # print the digits in the max_product_range
    for i in range(max_product_range[0], max_product_range[1] + 1):
        print(list_digits[i], end = " ")
    print()
    print(f'Range of Adjacent Max Product: {max_product_range}')
