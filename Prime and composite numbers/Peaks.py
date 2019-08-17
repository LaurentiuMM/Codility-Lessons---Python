import time


# <<< start solution


def is_ok(block_count, N, peak_count):
	block_size = int(N / block_count)
	if peak_count[block_size - 1] == 0:
		return False

	for block in range(2, block_count + 1):
		if peak_count[block * block_size - 1] == peak_count[(block - 1) * block_size - 1]:
			return False

	return True


def solution(A):
	N = len(A)

	peak_count = [0] * N

	for i in range(1, N - 1):
		peak_count[i] = peak_count[i - 1]
		if A[i] > max(A[i - 1], A[i + 1]):
			peak_count[i] += 1

	if N > 1:
		peak_count[N - 1] = peak_count[N - 2]

	for block_count in range(int(N / 2), 0, -1):
		if N % block_count == 0 and is_ok(block_count, N, peak_count):
			return block_count

	return 0


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
