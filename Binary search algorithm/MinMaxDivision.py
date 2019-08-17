import time


# <<< start solution

def get_block_count(A, largest_sum):
	block_count = 0
	per_block_sum = A[0]

	for i in range(1, len(A)):
		if per_block_sum + A[i] > largest_sum:
			block_count += 1
			per_block_sum = A[i]
		else:
			per_block_sum += A[i]

	block_count += 1

	return block_count


def solution(K, M_ignored, A):
	lower_bound = max(A)
	upper_bound = sum(A)

	result = lower_bound
	while lower_bound <= upper_bound:
		largest_sum = (lower_bound + upper_bound) // 2
		actual_block_count = get_block_count(A, largest_sum)
		if actual_block_count <= K:
			result = largest_sum
			upper_bound = largest_sum - 1
		else:
			lower_bound = largest_sum + 1

	return result


# end solution >>>


start_time = time.time()

# <<< start testing

K = [3, 2, 3, 3]
M = [5, 5, 6, 3]
A = [[2, 1, 5, 1, 2, 2, 2], [5, 3], [5, 2, 3, 4, 6], [1, 3, 1, 3, 2, 1, 3]]

result = [solution(k, m, a) for k, m, a in zip(K, M, A)]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
