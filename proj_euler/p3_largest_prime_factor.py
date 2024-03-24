
# Prime Factors of 13195: 5, 7, 13, 29
def prime_factorization(num):
    og_num = num
    prime_factors = []
    i = 2
    f = og_num // 2
    while i*2 <= num:
        if num % i == 0:
            prime_factors.append(i)
            num //= i
        else:
            i += 1
    prime_factors.append(num)
    return prime_factors

if __name__ == '__main__':
    num = 600851475143
    prime_factors = prime_factorization(num)
    print(prime_factors)
    print(max(prime_factors))