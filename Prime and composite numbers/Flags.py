def get_peaks(A):
	peaks = [False] * len(A)
	for i in range(1, len(A) - 1):
		if A[i] > max(A[i - 1], A[i + 1]):
			peaks[i] = True

	return peaks


def get_next_peaks(peaks):
	next = [0] * len(peaks)
	next[len(peaks) - 1] = -1
	for i in range(len(peaks) - 2, -1, -1):
		if peaks[i]:
			next[i] = i
		else:
			next[i] = next[i + 1]

	return next


def solution(A):
	peaks = get_peaks(A)
	next_peaks = get_next_peaks(peaks)

	max_k = 0
	k = 1

	while k * (k - 1) < len(peaks):
		flags = 0
		pos = 0
		while pos < len(peaks) and flags < k:
			pos = next_peaks[pos]
			if pos == -1:
				break
			flags += 1
			pos += k

		max_k = max(max_k, flags)
		k += 1

	return max_k


A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
result = solution(A)

print(result)
