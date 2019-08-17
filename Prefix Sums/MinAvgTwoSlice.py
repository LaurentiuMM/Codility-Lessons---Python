import time


# <<< start solution

import sys

def solution(A):
	N = len(A)

	min_avg = sys.maxsize
	min_ind = 0

	for i in [2, 3]:
		for j in range(0, N - i + 1):
			avg = sum(A[j:j + i]) / i
			if min_avg > avg:
				min_avg = avg
				min_ind = j

	return min_ind


# end solution >>>


start_time = time.time()

# <<< start testing

A = [4, 2, 2, 5, 1, 5, 8]
A = [4, -2, 2, -5, 2, 7, 8]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
