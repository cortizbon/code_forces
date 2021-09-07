n = int(input('Ingrese la info: '))

if n/5 > n // 5:
	pasos = int((n//5) + 1)
else:
	pasos = int(n/5)


print(pasos)
