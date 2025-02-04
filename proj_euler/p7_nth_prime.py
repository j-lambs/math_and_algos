
def get_Nth_prime(n: int) -> int:
	list_primes = [2, 3]

	# special case where user is asking for 1st or 2nd prime
	if n == 1 or n == 2:
		return list_primes[n - 1]

	next_prime = list_primes[len(list_primes) - 1]	# set next_prime to end of list_primes, which = 3
	# loop while we havent added the next prime
	while len(list_primes) != n:
		next_prime += 2
		if is_prime(next_prime, list_primes):
			list_primes.append(next_prime)
	# print(list_primes)
	return next_prime

# checks if n is evenly divisible by previous primes
def is_prime(n: int, list_primes: list) -> bool:
	n_sqrt = int(n**0.5)
	for prime in list_primes:
		if prime > n_sqrt: 	# an int multiple will be <= half of an int n - so if a prime is > half of n, then n is also prime
			return True
		if n % prime == 0:	# if n evenly divisible by a prime, it is not prime (is composite)
			return False
	return True

if __name__ == "__main__":
	n = 10001
	# n = 10
	print(get_Nth_prime(n)) 	# ~3.7 sec runtime @ n=10001
				# 173ms runtime @ n=10001 after changing is_prime to stop when the next prime is > the sqrt(n)
