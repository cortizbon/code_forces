l1 = list(input('Escriba la primera línea: '))
l2 = list(input('Escriba la segunda lìnea: '))

res = []

for i,j in zip(l1,l2):
	if i!=j:
		res.append('1')
	else:
		res.append('0')

print(''.join(res))
