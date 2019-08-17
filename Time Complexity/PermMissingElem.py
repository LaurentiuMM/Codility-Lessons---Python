import time


# <<< start solution

def solution(A):
	N = len(A)
	sum = int((N + 1) * (N + 2) / 2)

	for i in range(0, N):
		sum -= A[i]

	return sum


#  end solution >>>

start_time = time.time()

# <<< start testing

A = [2, 3, 1, 5]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
