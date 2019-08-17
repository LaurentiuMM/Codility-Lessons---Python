import time


# <<< start solution

def solution(A, B, K):
	return int(B / K) - int(A / K) + (1 if A % K == 0 else 0)


# end solution >>>


start_time = time.time()

# <<< start testing

A = 5
B = 12
K = 2
result = solution(A, B, K)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
