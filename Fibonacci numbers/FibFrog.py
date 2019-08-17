import time


# <<< start solution

import sys

def solution(A):
	N = len(A)
	fib = []

	if N == 0:
		return 1

	fib.append(1)
	fib.append(1)
	for i in range(2, N + 3):
		fib.append(fib[i - 1] + fib[i - 2])
		if fib[i] >= N + 1:
			break

	jump_no = 1
	min_jumps = [sys.maxsize] * (N + 2)
	steps = [-1]

	while jump_no <= N + 1:
		temp_steps = []
		for s in steps:
			for f in fib[1:]:
				pos = s + f
				if pos < N and A[pos] == 1:
					if min_jumps[pos] > jump_no:
						min_jumps[pos] = (0 if s == - 1 else min_jumps[s]) + 1
						temp_steps.append(pos)
				elif pos == N:
					min_jumps[pos] = (0 if s == - 1 else min_jumps[s]) + 1
					return min_jumps[pos]

		steps = temp_steps
		jump_no += 1

	return -1


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [], [1]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
