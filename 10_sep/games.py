n = int(input('Ingrese el número de equipos: '))

lista_colores = []

for _ in range(n):
	colores = input('Ingrese los colores: ').split(' ')
	lista_colores.append(colores)	

contador = 0
a0 = [i[0] for i in lista_colores]
a1 = [i[1] for i in lista_colores]	
for i in a1:
	for j in a0:
		if i==j:
			contador+=1
print(contador)
