import time


# <<< start solution

def is_triplet(P, Q, R):
	return P + Q > R and Q + R > P and R + P > Q


def solution(A):
	N = len(A)
	S = sorted(A)

	for i in range(0, N - 2):
		if is_triplet(S[i], S[i + 1], S[i + 2]):
			return 1

	return 0


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[10, 2, 5, 1, 8, 20]]
result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
