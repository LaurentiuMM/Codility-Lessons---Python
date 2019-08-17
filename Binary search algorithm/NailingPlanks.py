import time


# <<< start solution


def solution(A, B, C):
	N = len(A)
	M = len(C)

	prefix_sum = [0] * (2 * M + 1)

	if N == 0:
		return -1

	start = 0
	end = len(C)
	J = -1

	while start <= end:
		mid = (start + end) // 2

		prefix_sum[0:] = [0] * (2 * M + 1)

		for i in range(0, mid):
			prefix_sum[C[i]] += 1

		for i in range(1, len(prefix_sum)):
			prefix_sum[i] += prefix_sum[i - 1]

		covered = True
		for i in range(0, N):
			if prefix_sum[B[i]] == prefix_sum[A[i] - 1]:
				covered = False
				break

		if not covered:
			start = mid + 1
		else:
			end = mid - 1
			J = mid

	return J


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[1, 4, 5, 8], []]
B = [[4, 5, 9, 10], []]
C = [[4, 6, 7, 10, 2], [0, 1]]

result = [solution(a, b, c) for a, b, c in zip(A, B, C)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
