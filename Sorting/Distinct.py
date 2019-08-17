import time


# <<< start solution

def solution(A):
	return len(set(A))


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[2, 1, 1, 2, 3, 1]]
result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
