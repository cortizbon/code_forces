datos = input('Escriba los datos: ').split(' ')

n, k = int(datos[0]), int(datos[1])

for _ in range(k):
	if n%10==0:
		n = n / 10
	else:
		n = n - 1

print(int(n))
