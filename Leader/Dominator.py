import time


# <<< start solution

def solution(A):
	counter = dict()
	max_count = 0;
	max_ind = 0;

	for i, v in enumerate(A):
		if v in counter:
			counter[v] += 1
		else:
			counter[v] = 1

		max_count = max(max_count, counter[v])
		if max_count == counter[v]:
			max_ind = i

	return max_ind if max_count > len(A) / 2 else -1


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[3, 4, 3, 2, 3, -1, 3, 3]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
