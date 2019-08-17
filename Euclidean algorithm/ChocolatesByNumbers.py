import time


# <<< start solution

def get_gcd(a, b):
	if a % b == 0:
		return b
	else:
		return get_gcd(b, a % b)


def solution(N, M):
	if N % M == 0:
		return N // M

	gcd = get_gcd(N, M)

	return N // gcd


# end solution >>>


start_time = time.time()

# <<< start testing

N = [10, 1, 14, 28, 12]
M = [4, 1, 6, 8, 21]

result = [solution(*n) for n in zip(N, M)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
