n = int(input('Ingrese el número de imanes: '))

posiciones = []

for i in range(n):
	posiciones.append(list(input('Ingrese posición: ')))

contador = 1
for pos, posicion in enumerate(posiciones[:-1]):
	if int(posicion[1]) + int(posiciones[pos+1][0])!=1:
		contador += 1
print(contador)
