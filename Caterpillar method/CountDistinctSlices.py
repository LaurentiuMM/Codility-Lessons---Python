import time


# <<< start solution


def solution(M, A):
	N = len(A)

	uniques = set()
	front = 0
	slice_count = 0

	for back in range(0, N):
		while front < N and A[front] not in uniques:
			uniques.add(A[front])
			slice_count += len(uniques)
			front += 1
			if slice_count >= 1000000000:
				return 1000000000

		uniques.remove(A[back])

	return slice_count


# end solution >>>


start_time = time.time()

# <<< start testing

M = [6, 4]
A = [[3, 4, 5, 5, 2], [3]]

result = [solution(m, a) for m, a in zip(M, A)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
