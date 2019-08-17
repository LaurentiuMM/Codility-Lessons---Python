import time


# <<< start solution

def get_leader(A):
	counter = dict()
	max_count = 0
	max_val = 0

	for i, v in enumerate(A):
		if v in counter:
			counter[v] += 1
		else:
			counter[v] = 1

		max_count = max(max_count, counter[v])
		if max_count == counter[v]:
			max_val = v

	return max_val if max_count > len(A) / 2 else None


def solution(A):
	N = len(A)
	counter = [0] * N
	equi_count = 0

	leader = get_leader(A)

	if leader is None:
		return 0

	counter[0] = 1 if A[0] == leader else 0
	for i in range(1, N):
		counter[i] = counter[i - 1] + (1 if A[i] == leader else 0)

	for i in range(0, N - 1):
		if counter[i] > int((i + 1) / 2) and counter[N - 1] - counter[i] > int((N - i - 1) / 2):
			equi_count += 1

	return equi_count


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[4, 3, 4, 4, 4, 2]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
