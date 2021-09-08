n = int(input('Número de partidas jugadas: '))

resultados = list(input('Resultados: '))

A = 0
D = 0
for letra in resultados:
	if letra=='A':
		A+=1
	else:
		D+=1

if A>D:
	print('Anton')
elif D>A:
	print('Danika')
else:	
	print('Friendship')
