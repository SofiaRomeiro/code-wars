def dig(n1, n2):

	i = -1
	isn1s = len(n1) < len(n2) 
	sl = (len(n1) if len(n1) < len(n2) else len(n2))
	res = ''

	while i >= (-1 * sl):

		sum_  = eval(n1[i]) + eval(n2[i]) 

		

		if sum_ >= 10:
			res = str(sum_ % 10) + res

		else:
			res = str(sum_) + res

		i -= 1

	if isn1s:
		res = n2[:i+1] + res

	else: 
		res = n1[:i+1] + res

	return int(res)

n1 = input()
n2 = input()
print(dig(n1, n2))








