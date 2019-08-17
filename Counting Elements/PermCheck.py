import time


# <<< start solution

def solution(A):
	N = len(A)
	counts = [0] * (N + 1)

	for i in range(0, N):
		if A[i] > N:
			return 0
		else:
			counts[A[i]] += 1

	for i in range(1, N + 1):
		if counts[i] == 0:
			return 0

	return 1


#  end solution >>>


start_time = time.time()

# <<< start testing

A = [4, 1, 2, 3]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
