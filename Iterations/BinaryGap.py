import time

# <<< start solution
from math import log


def solution(N):
	i = int(log(N, 2))
	x = []
	while N > 0:
		if N >= 2 ** i:
			N -= 2 ** i
			x.append(i)

		i -= 1

	max_gap = 0

	for i in range(0, len(x) - 1):
		max_gap = max(max_gap, x[i] - x[i + 1] - 1)

	return max_gap


#  end solution >>>

start_time = time.time()

# <<< start testing

N = 32
result = solution(N)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
