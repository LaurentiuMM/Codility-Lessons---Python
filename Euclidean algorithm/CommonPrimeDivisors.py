import time


# <<< start solution

def get_gcd(a, b):
	if a % b == 0:
		return b
	else:
		return get_gcd(b, a % b)


def remove_common_prime_divisors(a, b):
	while a != 1:
		gcd = get_gcd(a, b)
		if gcd == 1:
			break
		a /= gcd

	return a

def has_same_prime_divisors(a, b):
	gcd = get_gcd(a, b)

	a = remove_common_prime_divisors(a, gcd)
	if a != 1:
		return False

	b = remove_common_prime_divisors(b, gcd)
	if b != 1:
		return False

	return True

def solution(A, B):
	Z = len(A)
	count = 0

	for i in range(0, Z):
		if has_same_prime_divisors(A[i], B[i]):
			count += 1

	return count


# end solution >>>


start_time = time.time()

# <<< start testing

A = [15, 10, 9, 1]
B = [75, 30, 5, 1]

result = [solution(A, B)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
