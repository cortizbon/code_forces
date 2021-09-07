matriz = []

for _ in range(5):
	matriz.append(input('Escriba la fila: ').split(' '))
pasos = 0

for fila in matriz:
	if '1' in fila:
		n = matriz.index(fila)
		pasos = abs(2-n)
		for columna in fila:
			if columna == '1':
				n = fila.index(columna)
				pasos = pasos + abs(2-n)
				break
		break
	else:
		None


print(pasos)
