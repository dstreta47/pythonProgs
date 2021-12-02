
def LadderProblemUtil(n, m):
	if n <= 1:
		return n
	res = 0
	i = 1
	while i<= m and i<= n:
		res = res + LadderProblemUtil(n-i, m)
		i = i + 1
	return res

def LadderProblem(s, m):
	return LadderProblemUtil(s + 1, m)
s, m = 2, 3
print(LadderProblem(s, m))
