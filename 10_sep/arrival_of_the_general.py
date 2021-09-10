n = int(input('Ingrese el número de datos: '))
datos = [int(i) for i in input('Ingrese los datos: ').split(' ')]

maxim = 2
minim = 100

for pos,num in enumerate(datos):
	if num > maxim:
		maxim = num
		posmax = pos
	if num <= minim:
		minim = num
		posmin = pos
if posmax - posmin == -1:
	movs = posmax-0 + (abs(posmin-(len(datos)-1)))
	print(movs)
else:
	movs = posmax - 0 +(abs(posmin-(len(datos)-1)))-1
	print(movs)

