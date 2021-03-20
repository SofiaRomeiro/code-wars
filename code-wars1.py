def regex(s, pattern, closed):

	if (s == ''):
		result = ''
		for p in pattern:
			result += p
		return result

	elif ord('(') == ord(s[0]):
		pattern.append('')
		return regex(s[1:], pattern, False)

	elif ord(')') == ord(s[0]):
		if closed:
			pattern[-2] += pattern[-1]
			return regex(s[1:], pattern[:-1], True)
		return regex(s[1:], pattern, True)

	elif (ord(s[0]) == ord('*')) or (ord(s[0]) == ord('?')):
		if (closed):
			return regex(s[1:], pattern[:-1], False)
		elif not closed and len(pattern) == 1:
			pattern[-1] = pattern[-1][:-1]
			return regex(s[1:], pattern, False)
		else:
			pattern[-2] += pattern[-1][:-1]
			return regex(s[1:], pattern[:-1], False)

	elif ord(s[0]) == ord('+'):
		pattern[-2] += pattern[-1]
		return regex(s[1:], pattern[:-1], False)

	else:
		pattern[-1] += s[0]
		return regex(s[1:], pattern, False)

s = input()
#print(regex(s, [''], False))

contexts = ['']
output = ''
closed = False

while s != '':
	c = s[0]

	if ord(c) == ord('('):
		contexts.append('')

	elif ord(c) == ord(')'):
		if closed:
			contexts[-2] += contexts[-1]
			contexts = contexts[:-1] 
		closed = True 


	elif ord(c) == ord('*') or ord(c) == ord('?'):

		if not closed and len(contexts) > 1:
			contexts[-2] += contexts[-1][:-1]

		elif not closed:
			contexts[-1] = contexts[-1][:-1]

		else:
			contexts = contexts[:-1]
		closed = False

	elif ord(c) == ord('+'):
		if len(contexts) > 1:
			contexts[-2] += contexts[-1]
		else:
			contexts[0] += c

		closed = False

	else:
		if closed:
			contexts[-2] += contexts[-1]
			contexts = contexts[:-1]

		contexts[-1] += c
		closed = False

	s = s[1:]

print(contexts)


