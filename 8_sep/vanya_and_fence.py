datos = input('Ingrese número de amigos y altura: ').split()

n, h = int(datos[0]), int(datos[1])

alturas = input('Ingrese las alturas: ').split(' ')

width = 0
for i in alturas:
	if int(i)>h:
		width+=2
	else:
		width+=1

print(width)
