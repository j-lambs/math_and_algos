
def int_is_palindrome(num: int) -> bool:
    num = str(num)
    p1 = 0
    p2 = len(num) - 1

    # even num of digits
    if len(num) % 2 == 0:
        while p1 < p2:
            if num[p1] == num[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
    # odd num of digits
    else:
        while p1 != p2:
            if num[p1] == num[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    largest_product = 0
    multipliers = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            temp_product = i * j
            if temp_product > largest_product and int_is_palindrome(temp_product):
                largest_product = temp_product
                multipliers = [i, j]

    print(f'{multipliers[0]} * {multipliers[1]} = {largest_product}')
