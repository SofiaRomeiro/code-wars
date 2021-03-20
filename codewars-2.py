def fizzbuzz(n):
	n1, n2 = 0, 1
	cad = ''
	i = 0
	val = 1

	if n == 1:
		print('1')

	while i < n:
		if n1 % 3 == 0 and i != 0:
			if n1 % 5 == 0:
				cad += 'fizzbuzz '
			else:
                cad += 'fizz '
        elif n1 % 5 == 0 and i != 0:
            cad += 'buzz '
        else:
            cad += str(n1) + ' '

        val = n1 + n2

        n1 = n2
        n2 = val
        i += 1

    return cad

n = int(input())
print(fizzbuzz(n))