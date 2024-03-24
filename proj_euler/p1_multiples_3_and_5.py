# If we list all the natural numbers below $10$ that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Learned:
# 'integer division' (operator '//') in Python is floating point division, then using floor()

# 1st attempt - go through all nums (1-limit) and add if multiple of 3 or 5
def sum_3_and_5_brute_force(limit):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# attempt 2 - calculate number of multiples of 3 & 5, then distributes factor to the sum
def num_multiples(limit):
    sum_total = attempt2_helper(limit, 3) + attempt2_helper(limit, 5) - attempt2_helper(limit, 15)
    return sum_total
    # is there a way to do it in 1 loop?

def attempt2_helper(limit, factor):
    num_multiples = (limit - 1) // factor   # get num of multiples of factor below < limit
    sum = 0
    for i in range(1, num_multiples + 1):
        sum += i
    return factor * sum

# attempt 3 - triangular numbers
# triangular numbers are like factorial but w addition
# T1 = 1, T2 = 3, T3 = 6, T4 = 10, T5 = 15, T6 = 21
# get nth tri number is (n*(n+1))/2
# or its c(n+1, 2)
def triangular_nums(limit):
    return 3 * get_nth_trinagular_num((limit - 1) // 3) + 5 * get_nth_trinagular_num((limit - 1) // 5) - 15 * get_nth_trinagular_num((limit - 1) // 15)
def get_nth_trinagular_num(n):
    return (n * (n + 1)) / 2

if __name__ == '__main__':
    limit = 1000000     
    # if limit = a milli - 233333166668

    # print(f'Sum Brute Force: {sum_3_and_5_brute_force(limit)}') # 225 229 206 225 204 (ms)
    # print(f'Sum Attempt 2: {num_multiples(limit)}')          # 117 109 118 122 113 (ms)
    print(f'Sum Triangle Nums: {int(triangular_nums(limit))}')  # 67 62 64 63 62 (ms)

