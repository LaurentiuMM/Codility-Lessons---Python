import time


# <<< start solution

def solution(A):
	N = len(A)
	divisor_count = [0] * (2 * N + 1)
	counter = [0] * (2 * N + 1)

	for i in range(0, N):
		counter[A[i]] += 1

	set_A = set(A)

	for v in set_A:
		pos = v
		while pos <= 2 * N:
			divisor_count[pos] += counter[v]
			pos += v

	non_divisor_count = []

	for i in range(0, N):
		non_divisor_count.append(len(A) - divisor_count[A[i]])

	return non_divisor_count


#  end solution >>>

start_time = time.time()

# <<< start testing

A = [3, 1, 2, 3, 6]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
