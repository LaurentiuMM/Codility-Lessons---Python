import time


# <<< start solution


def solution(A, K):
	N = len(A)

	if N == 0 or K == N or K == 0:
		return A

	for i in range(0, K):
		last = A[N - 1]
		for j in range(N - 1, -1, -1):
			A[j] = A[j - 1]
		A[0] = last

	return A


#  end solution >>>

start_time = time.time()

# <<< start testing

A = [3, 8, 9, 7, 6]
K = 3
result = solution(A, K)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
