import time


# <<< start solution

import sys

def solution(A):
	curr_sum = 0
	max_sum = - sys.maxsize

	for x in A:
		curr_sum += x
		max_sum = max(max_sum, curr_sum)
		if curr_sum < 0:
			curr_sum = 0

	return max_sum


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[3, 2, -6, 4, 0], [-2, 1]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
