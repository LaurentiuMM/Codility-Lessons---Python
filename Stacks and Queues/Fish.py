import time


# <<< start solution

def solution(A, B):
	N = len(A)
	river = []
	alive = 0

	for i in range(0, N):
		if B[i] == 1:
			river.append(i)
		else:
			while len(river) > 0 and A[river[len(river) - 1]] < A[i]:
				river.pop()
			if len(river) == 0:
				alive += 1

	alive += len(river)

	return alive


# end solution >>>


start_time = time.time()

# <<< start testing

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

result = solution(A, B)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
