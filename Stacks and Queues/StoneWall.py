import time


# <<< start solution

def solution(H):
	stack = []
	count = 0

	for h in H:
		while len(stack) > 0 and h < stack[len(stack) - 1]:
			stack.pop()
		if len(stack) == 0 or h > stack[len(stack) - 1]:
			stack.append(h)
			count += 1

	return count


# end solution >>>


start_time = time.time()

# <<< start testing

H = [[8, 8, 5, 7, 9, 8, 7, 4, 8]]

result = [solution(h) for h in H]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
