datos = input('Escriba los datos: ').split(' ')

limak, bob = int(datos[0]), int(datos[1])
contador=0

while limak <= bob:
	contador += 1
	limak *= 3
	bob *= 2

print(contador)
