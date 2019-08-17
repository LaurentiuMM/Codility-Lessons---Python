import time


# <<< start solution

import sys

def solution(N):
	min_perimeter = sys.maxsize

	i = 1
	while i * i <= N:
		if N % i == 0:
			min_perimeter = min(min_perimeter, i + int(N / i))
		i += 1

	return 2 * min_perimeter


# end solution >>>


start_time = time.time()

# <<< start testing

N = [30, 1]

result = [solution(n) for n in N]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
