n = int(input('Ingrese el número de amigos: '))

datos = input('Ingrese los datos: ').split(' ')

comb = []

for pos, i in enumerate(datos):
	comb.append((int(i),pos+1))

comb.sort()

result = [str(i[1]) for i in comb]

print(' '.join(result))
#organizar la tupla a partir de i
