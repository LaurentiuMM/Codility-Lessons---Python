import time


# <<< start solution

def solution(A):
	N = len(A)
	S = sorted(A)

	products = []

	products.append(S[N - 1] * S[N - 2] * S[N - 3])
	products.append(S[N - 1] * S[0] * S[1])
	products.append(S[0] * S[1] * S[2])

	return max(products)


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[-3, -2, 1, 2, 5, 6],
	 [-10, -5, -3, -2, 3],
	 [-10, -5, -3, 2, 3],
	 [-10, -5, -4, -3, -2]]
result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
