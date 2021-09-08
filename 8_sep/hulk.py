n = int(input('Ingrese el número de capas: '))

res = 'I hate'
contador = 1

while contador < n:
	contador += 1
	if contador%2==0:
		res = res + ' that I love'
	else:
		res = res + ' that I hate' 

print(res + ' it')

