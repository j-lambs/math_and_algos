# v1: [Finished in 148.9s]
# basic iterative approach
# optimization: 
#   check_power_of_2 method

def collatz_seq_len(start):
    cur = start
    seq_len = 0
    while True:
        pow_two = check_power_of_2(cur)
        if pow_two:
            return seq_len + pow_two
        if cur % 2 == 0:
            cur = int(cur / 2)
        else:
            cur = cur * 3 + 1
        seq_len += 1


def check_power_of_2(n):
    """
    :param n: an integer
    :return: the power of 2 if power of 2
                or false if not power of 2
    """
    bin_str = str(bin(n))[2:]   # convert n to binary and remove 0b in front
    if (bin_str[0] == '1' and int(bin_str[1:])) == 0:
        power = len(bin_str)
        return power
    return False
def longest_collatz_seq():
    longest_collatz_len = 0
    longest_collatz_n = 0
    for i in range(2, 1000000):
        temp = collatz_seq_len(i)
        if temp > longest_collatz_len:
            longest_collatz_len = temp
            longest_collatz_n = i
    return (longest_collatz_n, longest_collatz_len)

print(longest_collatz_seq())
# print(collatz_seq_len(9))

