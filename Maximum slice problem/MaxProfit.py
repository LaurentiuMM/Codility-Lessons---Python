import time


# <<< start solution

def solution(A):
	N = len(A)
	max_profits = [0] * N

	if len(A) == 0:
		return 0

	min_price = A[0]
	for i in range(1, N):
		max_profits[i] = max(max_profits[i - 1], A[i] - min_price)
		min_price = min(min_price, A[i])

	return max_profits[N - 1] if max_profits[N - 1] > 0 else 0


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[23171, 21011, 21123, 21366, 21013, 21367]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
