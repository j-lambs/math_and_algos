
if __name__ == '__main__':
    MAX = 4000000
    left = 1
    right = 2
    next_fib = left + right
    sum = right

    while next_fib <= MAX:
        if next_fib % 2 == 0:
            sum += next_fib
        left = right
        right = next_fib
        next_fib = left + right

    print(f'Sum: {sum}')