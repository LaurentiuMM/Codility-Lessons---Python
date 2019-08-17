import time


# <<< start solution

def solution(A):
	N = len(A)
	sum_starting = [0] * N
	sum_ending = [0] * N

	for i in range(1, N - 1):
		sum_ending[i] = max(sum_ending[i - 1] + A[i], A[i])

	for i in range(N - 2, 0, -1):
		sum_starting[i] = max(sum_starting[i + 1] + A[i], A[i])

	max_slice = 0
	for i in range(1, N - 1):
		max_slice = max(max_slice, sum_ending[i - 1] + sum_starting[i + 1])
		max_slice = max(max_slice, sum_starting[i + 1])
		max_slice = max(max_slice, sum_ending[i - 1])

	return max_slice


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[3, 2, 6, -1, 4, 5, -1, 2], [0, 10, -5, -2, 0], [6, 1, 5, 6, 4, 2, 9, 4]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
