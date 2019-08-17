import time


# <<< start solution


def solution(A):
	N = len(A)
	leftovers = set()

	for i in range(0, N):
		if A[i] in leftovers:
			leftovers.remove(A[i])
		else:
			leftovers.add(A[i])

	return list(leftovers)[0];


#  end solution >>>

start_time = time.time()

# <<< start testing

A = [9, 3, 9, 3, 9, 7, 9]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
