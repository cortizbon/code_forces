n = int(input('Número de rocas: '))
s = list(input('Color de las rocas: '))

contador = 0
for pos,i in enumerate(s[:-1]):
	if i == s[pos+1]:
		contador += 1

print(contador)
