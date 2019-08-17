import time


# <<< start solution

def solution(A):
	N = len(A)

	if N == 0:
		return 0

	uniques = [A[0]]
	for x in A[1:]:
		if x != uniques[len(uniques) - 1]:
			uniques.append(x)

	count = 0
	start = 0
	end = len(uniques) - 1

	while start < end:
		if abs(uniques[start]) != abs(uniques[end]):
			count += 1
			if abs(uniques[start]) < abs(uniques[end]):
				end -= 1
			else:
				start += 1
		else:
			start += 1

	return count + 1 if N > 0 else 0


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[-5, -3, -1, 0, 3, 6], [], [1], [-1, 1, 2], [-3, -2, -2, 1, 3, 4]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
