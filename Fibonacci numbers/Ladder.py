import time


# <<< start solution

def solution(A, B):
	a_max = max(A)
	b_max = max(B)
	fib = [0] * (a_max + 2)

	fib[1] = 1
	for i in range(2, a_max + 2):
		fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << b_max) - 1)

	return [fib[a + 1] & ((1 << b) - 1) for a, b in zip(A, B)]


# end solution >>>


start_time = time.time()

# <<< start testing

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]

result = [solution(A, B)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
