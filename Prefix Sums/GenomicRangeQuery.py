import time


# <<< start solution

def solution(S, P, Q):
	N = len(S)

	impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

	answers = []

	A_counter = [0] * N
	C_counter = [0] * N
	G_counter = [0] * N
	T_counter = [0] * N

	A_temp = 0
	C_temp = 0
	G_temp = 0
	T_temp = 0

	for i, n in enumerate(S):
		if n == "A":
			A_temp += 1
		elif n == "C":
			C_temp += 1
		elif n == "G":
			G_temp += 1
		elif n == "T":
			T_temp += 1

		A_counter[i] = A_temp
		C_counter[i] = C_temp
		G_counter[i] = G_temp
		T_counter[i] = T_temp

	for p, q in zip(P, Q):
		if p == q:
			answers.append(impact[S[p]])
		else:
			ans = 0

			if A_counter[q] - (A_counter[p - 1] if p > 0 else 0) > 0:
				ans = 1
			elif C_counter[q] - (C_counter[p - 1] if p > 0 else 0) > 0:
				ans = 2
			elif G_counter[q] - (G_counter[p - 1] if p > 0 else 0) > 0:
				ans = 3
			elif T_counter[q] - (T_counter[p - 1] if p > 0 else 0) > 0:
				ans = 4

			answers.append(ans)

	return answers


# end solution >>>


start_time = time.time()

# <<< start testing

S = "CAGCCTA"
P = [2, 5, 0, 2]
Q = [4, 5, 6, 3]
result = solution(S, P, Q)

print(result)

# end testing >>>

end_time = time.time()
print("Time: " + str(end_time - start_time))
