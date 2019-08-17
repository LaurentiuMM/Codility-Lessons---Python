import time


# <<< start solution

def solution(X, Y, D):
	t = int((Y - X) / D)

	return t if (Y - X) % D == 0 else t + 1


#  end solution >>>

start_time = time.time()

# <<< start testing

X = 10
Y = 85
D = 30
result = solution(X, Y, D)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
