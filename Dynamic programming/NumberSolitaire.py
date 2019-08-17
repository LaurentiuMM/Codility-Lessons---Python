import time


# <<< start solution
import sys

def solution(A):
	N = len(A)

	dp = [-sys.maxsize] * N
	dp[0] = A[0]

	for j in range(1, N):
		for i in range(1, 7):
			if j >= i:
				dp[j] = max(dp[j], dp[j - i] + A[j])

	return dp[N - 1]


# end solution >>>


start_time = time.time()

# <<< start testing

A = [[1, -2, 0, 9, -1, -2], [-8, 4]]

result = [solution(a) for a in A]

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
