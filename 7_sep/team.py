n = int(input('Escriba el número de problemas: '))
lista_problemas = []
for _ in range(n):
	lista_problemas.append(input('Escriba quién está seguro de solucionar el problema: '))
contador = 0
for problema in lista_problemas:
	lista =  problema.split(' ')
	seguros = sum([int(i) for i in lista])
	if seguros >= 2:
		contador +=1
	else:
		None

print(contador) 	


