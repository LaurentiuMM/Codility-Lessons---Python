import time


# <<< start solution

def solution(A):
	N = len(A)

	if N == 1:
		return abs(2 * A[0])

	A.sort()

	start = 0
	end = N - 1
	min_abs = abs(2 * A[start])
	min_abs = min(min_abs, abs(2 * A[end]))

	while start <= end:
		min_abs = min(min_abs, abs(A[start] + A[end]))
		if abs(A[start]) > abs(A[end]):
			start += 1
		else:
			end -= 1

	return min_abs


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[1, 4, -3], [-8, 4, 5, -10, 3], [1], [-1], [1, 2]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
