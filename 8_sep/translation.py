s = input('Palabra: ')
t = input('Traducción: ')

if s[::-1] == t:
	print('YES')
else:
	print('NO')
