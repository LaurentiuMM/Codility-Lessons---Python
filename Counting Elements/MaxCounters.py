import time


# <<< start solution

def solution(N, A):
	M = len(A)
	counters = [0] * N
	max_counter = 0
	min_counter = 0

	for i in range(0, M):
		if A[i] <= N:
			if counters[A[i] - 1] < min_counter:
				counters[A[i] - 1] = min_counter
			counters[A[i] - 1] += 1
			max_counter = max(max_counter, counters[A[i] - 1])
		else:
			min_counter = max_counter

	for i in range(0, N):
		if counters[i] < min_counter:
			counters[i] = min_counter

	return counters


#  end solution >>>


start_time = time.time()

# <<< start testing

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
result = solution(N, A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
