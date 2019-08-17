import time


# <<< start solution

def solution(S):
	stack = []
	counterparts = {')': '(', ']': '[', '}': '{'}

	for x in S:
		if x in ["(", "[", "{"]:
			stack.append(x)
		else:
			if len(stack) > 0 and stack[len(stack) - 1] == counterparts[x]:
				stack.pop()
			else:
				return 0

	return 1 if len(stack) == 0 else 0


# end solution >>>


start_time = time.time()

# <<< start testing

A = ["{[()()]}", "([)()]", ")("]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
