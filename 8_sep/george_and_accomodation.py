n = int(input('Ingrese el número de habitaciones: '))

combinaciones = []
for i in range(n):
	combinaciones.append(input('Ingrese los datos: ').split(' '))

contador = 0

for ocup, capa in combinaciones:
	if int(capa)-int(ocup)>=2:
		contador += 1

print(contador)
