# <<< start solution
import sys
import time


def solution(A):
	N = len(A)
	sums = [0] * N
	sums[0] = A[0]

	for i in range(1, N):
		sums[i] = sums[i - 1] + A[i]

	min_diff = sys.maxsize

	for i in range(0, N - 1):
		min_diff = min(min_diff, abs(2 * sums[i] - sums[N - 1]))

	return min_diff


#  end solution >>>


start_time = time.time()

# <<< start testing

A = [3, 1, 2, 4, 3]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
