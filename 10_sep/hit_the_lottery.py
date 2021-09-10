n = int(input('Ingrese la cantidad a retirar: '))

contador = 0

dens = [100,20,10,5,1]

for den in dens:
	if n!=0:
		contador = contador + n//den
		n = n - (den* (n//den))
	else:
		break

print(contador)

