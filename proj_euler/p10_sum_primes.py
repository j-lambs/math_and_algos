import p7_nth_prime

# MAX = 2000000
# MAX = 8000
# MAX = 10
MAX = 100
"""
# uses get_Nth_prime() function from Problem 7
# but this is slow bc that function builds the primes everytime it is called
"""
def attempt1():
    next_prime = 0
    sum = 0
    i = 1   # counter
    prime_list = []

    while next_prime < MAX:
        next_prime = p7_nth_prime.get_Nth_prime(i)
        sum += next_prime
        prime_list.append(next_prime)
        print((i, next_prime), end=" ")
        i += 1

    prime_list.pop()
    sum -= next_prime
    print(prime_list)
    print(f'Num primes < {MAX}: {len(prime_list)}')
    return sum

"""
Propery of Primes: All primes > 3 can be expressed as ( 6n ± 1 ), where n ϵ N
"""
def sum_primes_below_max(max: int) -> int:
    # Special Cases bc ADHD
    if max <= 2:
        raise Exception("MAX must be > 2.") 
    if max == 3:
        return 2
    if max < 5:
        return 2 + 3

    prime_list = [2, 3]
    sum = 2 + 3
    n = 1
    next_prime = 3

    while next_prime < max:
        temp1 = 6 * n - 1
        temp2 = temp1 + 2

        if p7_nth_prime.is_prime(temp1, prime_list):
            prime_list.append(temp1)
            sum += temp1
        if p7_nth_prime.is_prime(temp2, prime_list):
            prime_list.append(temp2)
            sum += temp2
        next_prime = prime_list[len(prime_list) - 1]
        n += 1

    # check and remove if we added primes greater than max, and subtract off sum
    i = 0
    while i < 2:
        last_prime = prime_list[len(prime_list) - 1]
        if last_prime > max:
            sum -= last_prime
            prime_list.pop()
            i += 1
        else:
            break

    print(prime_list)
    return sum

# realized that its slow bc p7_nth_prime.get_Nth_prime has to build the prime list every call lol
if __name__ == "__main__":
    
    print(f'Sum: {sum_primes_below_max(MAX)}')

    # print(f'Sum: {attempt1()}')
