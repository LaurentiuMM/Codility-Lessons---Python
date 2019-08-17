import time


# <<< start solution

def solution(A):
	N = len(A)
	passing_cars = [0] * N
	east_cars = 1 if A[0] == 0 else 0

	for i in range(1, N):
		if A[i] == 0:
			east_cars += 1
			passing_cars[i] = passing_cars[i - 1]
		else:
			passing_cars[i] = passing_cars[i - 1] + east_cars

	return passing_cars[N - 1] if passing_cars[N - 1] <= 1000000000 else -1


# end solution >>>


start_time = time.time()

# <<< start testing

A = [0, 1, 0, 1, 1]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
