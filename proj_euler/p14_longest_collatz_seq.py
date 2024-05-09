# v1: [Finished in 148.9s]
# basic iterative approach
# optimization: 
#   check_power_of_2 method

# v2: [Finished in 6.6s]
# put all values encountered in prev iterations into hashmap with corresponding collatz seq len

mymap = dict() # k: number, v: collatz seq length

def collatz_seq_len(start):
    total_len = 0    # collatz seq len of 'start'
    cur = start
    seq = [start]
    while True:
        pow_two = check_power_of_2(cur)
        if pow_two:
            total_len = len(seq) + pow_two
            break

        cur_collatz_len = mymap.get(cur)
        if cur_collatz_len != None:
            total_len = len(seq) + cur_collatz_len
            break
        if cur % 2 == 0:
            cur = int(cur / 2)
        else:
            cur = cur * 3 + 1
        seq.append(cur)

    # update hashmap
    for i in range(len(seq)):
        mymap.update({seq[i]: total_len - i})
    return total_len

def check_power_of_2(n):
    """
    :param n: an integer
    :return: the power of 2 if power of 2
                or false if not power of 2
    """
    bin_str = str(bin(n))[2:]   # convert n to binary and remove 0b in front
    if (bin_str[0] == '1' and int(bin_str[1:])) == 0:
        power = len(bin_str)
        return power - 1
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
# print(collatz_seq_len(13))