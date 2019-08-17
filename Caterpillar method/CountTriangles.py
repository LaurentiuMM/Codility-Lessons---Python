import time


# <<< start solution

def solution(A):
	N = len(A)
	count = 0

	A_sorted = sorted(A)

	for P in range(0, N - 2):
		Q = P + 1
		R = P + 2
		while R < N:
			if A_sorted[P] + A_sorted[Q] > A_sorted[R]:
				count += R - Q
				R += 1
			elif Q < R - 1:
				Q += 1
			else:
				R += 1
				Q += 1

	return count


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[10, 2, 5, 1, 8, 12], [], [1], [1, 2], [1, 2, 2]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
