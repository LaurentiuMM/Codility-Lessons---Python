import time


# <<< start solution

def get_sum(A):
	N = len(A)

	if N == 0:
		return 0
	elif N == 1:
		return abs(A[0])
	elif N == 2:
		return abs(A[0] - A[1])
	else:
		B = []
		C = []
		B_sum = 0
		C_sum = 0

		for x in A:
			if B_sum <= C_sum:
				B.append(x)
				B_sum += x
			else:
				C.append(x)
				C_sum += x

		return abs(get_sum(B) - get_sum(C))


def solution(A):
	A_abs_sorted = sorted([abs(x) for x in A], reverse=True)
	return get_sum(A_abs_sorted)


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[1, 5, 2, -2], [3, 3, 3, 4, 5], [], [4, 3]]

result = [solution(a) for a in A]
4
print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
