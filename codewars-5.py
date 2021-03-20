lista = [1,2,3]

last_num = 0
increase = 0

def smallest_num(lista):
	last_num = 0

	for x in range(0, 10):
		if x in lista:
			last_num = x
			return last_num

last_num = smallest_num(lista)

for i in lista:

	print(i, 'i')
	print(last_num, 'last_num')
	
	if last_num < i:
		increase += 1
		last_num = i
	elif last_num > i:
		last_num =  i
	else:
		pass


print(increase)