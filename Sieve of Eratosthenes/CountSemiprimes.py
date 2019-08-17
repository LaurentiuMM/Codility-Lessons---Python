import time


# <<< start solution

def get_semiprimes_sieve(N):
	semiprimes = [1] * (N + 1)
	factor_count = [0] * (N + 1)
	semiprimes[0] = semiprimes[1] = -1

	i = 2
	while i <= N / 2:
		if semiprimes[i] == 1:
			for k in range(i * 2, N + 1, i):
				factor_count[k] += 1
				if factor_count[k] > 2:
					semiprimes[k] = -1
				else:
					semiprimes[k] = semiprimes[k] * (k if k == i * i else i)
		i += 1

	return semiprimes


def get_semiprimes_counts(semiprimes_sieve):
	counts = [0] * len(semiprimes_sieve)

	for i in range(2, len(counts)):
		counts[i] = counts[i - 1] + (1 if semiprimes_sieve[i] == i else 0)

	return counts


def solution(N, P, Q):
	semiprimes_sieve = get_semiprimes_sieve(N)

	semiprime_counts = get_semiprimes_counts(semiprimes_sieve)

	result = []
	for i in range(0, len(P)):
		result.append(semiprime_counts[Q[i]] - semiprime_counts[P[i] - 1])

	return result


#  end solution >>>

start_time = time.time()

# <<< start testing

N = 1000
P = [1, 4, 16, 20]
Q = [26, 10, 20, 1000]
result = solution(N, P, Q)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
