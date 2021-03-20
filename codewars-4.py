def compare(n1, n2):
	ns1 : str = str(n1) 
	ns2 : str = str(n2)
	s1 : str = ''
	s2 : str = ''
	changes : int = 0 
	equals : list = []
	equalpos2_l : list = []
	
	if ns1 == ns2:
		return 0

	for c in range(len(ns1)):
		if ns1[c] != ns2[c]:
			s1 += ns1[c]
			s2 += ns2[c]

	def posiguais(s):
		equalpos_d : dict = {}
		equalpos_l : list = []
		for i in range(len(s)):
			if s[i] not in equalpos_d: # adicionar nova pos
				equalpos_d[s[i]] = [i]
			elif s[i] in equalpos_d: #ver que posicoes tem numeros iguais
				equalpos_d[s[i]] += [i]
		for key in equalpos_d:
			equalpos_l += [equalpos_d[key]]
		return equalpos_d, equalpos_l

	equalpos2_l = posiguais(s2)[1]

	return len(equalpos2_l)


n1 = input()
n2 = input()
print(compare(n1, n2))





























		














	

	





