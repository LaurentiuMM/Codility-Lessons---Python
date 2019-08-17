import time


# <<< start solution

def solution(A):
	N = len(A)

	S = [(j - v, j + v) for j, v in enumerate(A)]
	S = sorted(S, key=lambda v: v[0])
	S = [(x[0] if x[0] >= 0 else 0, x[1] if x[1] <= N - 1 else N - 1) for x in S]

	start = [0] * N
	end = [0] * N

	for x in S:
		start[x[0]] += 1
		end[x[1]] += 1

	count = 0
	open = 0

	for i in range(0, N):
		count += open * start[i] + int(start[i] * (start[i] - 1) / 2)
		open += start[i] - end[i]

		if count > 10000000:
			count = -1
			break

	return count


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[1, 5, 2, 1, 4, 0]]
result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
