import time


# <<< start solution

def solution(S):
	stack = []

	for s in S:
		if s == "(":
			stack.append(s)
		else:
			if len(stack) > 0:
				stack.pop()
			else:
				return 0

	return 1 if len(stack) == 0 else 0


# end solution >>>


start_time = time.time()

# <<< start testing

S = ["(()(())())", "())"]

result = [solution(s) for s in S]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
