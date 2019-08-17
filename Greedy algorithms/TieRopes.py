import time


# <<< start solution

def solution(K, A):
	N = len(A)

	length = 0
	count = 0

	for i in range(0, N):
		length += A[i]

		if length >= K:
			count += 1
			length = 0

	return count


# end solution >>>


start_time = time.time()

# <<< start testing

K = [4, 4, 3, 5, 3]
A = [[1, 2, 3, 4, 1, 1, 3], [4], [4], [3, 2], [3, 2]]

result = [solution(k, a) for k, a in zip(K, A)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
