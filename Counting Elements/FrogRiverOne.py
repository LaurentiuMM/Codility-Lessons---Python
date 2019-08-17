import time


# <<< start solution

def solution(X, A):
	N = len(A)
	fallen = [False] * (X + 1)
	sum_all = int(X * (X + 1) / 2)
	sum_check = 0;

	for i in range(0, N):
		if not fallen[A[i]]:
			fallen[A[i]] = True
			sum_check += A[i]
			if sum_check == sum_all:
				return i

	return -1


# end solution >>>


start_time = time.time()

# <<< start testing

X = 5
A = [1, 3, 1, 4, 2, 3, 4, 4]
result = solution(X, A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
