import time


# <<< start solution

def solution(A):
	uniques = set(A)

	for i in range(1, 1000000):
		if i not in uniques:
			return i

	return 1


#  end solution >>>


start_time = time.time()

# <<< start testing

A = [1, 3, 6, 4, 1, 2]
result = solution(A)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
