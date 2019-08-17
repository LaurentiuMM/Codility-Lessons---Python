import time


# <<< start solution

def solution(A, B):
	N = len(A)

	if N <= 1:
		return N

	count = 1
	last_B = B[0]

	for i in range(1, N):
		if A[i] > last_B:
			count += 1
			last_B = B[i]

	return count


# end solution >>>


start_time = time.time()


# <<< start testing

A = [[1, 3, 7, 9, 9], [], [1, 4], [2, 3]]
B = [[5, 6, 8, 9, 10], [], [3, 6], [3, 7]]

result = [solution(a, b) for a, b in zip(A, B)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
