datos = input('Ingrese estudiantes y segundos: ').split(' ')

n, t = int(datos[0]), int(datos[1])

orden = list(input('Ingrese el orden: '))

for s in range(t):
	for pos, nin in enumerate(orden[:-1]):
		if nin=='B' and orden[pos+1]=='G':
			 orden[pos], orden[pos+1] = orden[pos+1], orden[pos]
		else:
			None
print(''.join(orden))
