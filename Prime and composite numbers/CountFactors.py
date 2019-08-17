import time


# <<< start solution

def solution(N):
	count = 0
	i = 1

	if N == 1:
		return 1

	while i * i < N:
		if N % i == 0:
			count += 2
		i += 1

	if i * i == N:
		count += 1

	return count


# end solution >>>


start_time = time.time()

# <<< start testing

N = [24, 1, 4]

result = [solution(n) for n in N]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
