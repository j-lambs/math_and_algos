
def get_Nth_prime(n: int) -> int:
	list_primes = [2]

	next_prime = list_primes[len(list_primes) - 1]	# set next_prime to end of list_primes
	# loop while we havent added the next prime
	while len(list_primes) != n:
		next_prime += 1
		if is_prime(next_prime, list_primes):
			list_primes.append(next_prime)
	print(list_primes)
	return next_prime

# checks if n is evenly divisible by previous primes
def is_prime(n: int, list_primes: list) -> bool:
	half_n = n / 2
	for prime in list_primes:
		if prime > half_n: 	# an int multiple will be <= half of an int n - so if a prime is > half of n, then n is also prime
			return True
		if n % prime == 0:	# if n evenly divisible by a prime, it is not prime (is composite)
			return False
	return True

if __name__ == "__main__":
	n = 10001
	print(get_Nth_prime(n)) 	# ~3.7 sec runtime @ n=10001
