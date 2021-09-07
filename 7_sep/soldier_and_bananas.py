datos = input('Ingrese los valores: ').split(' ')

k, n, w = int(datos[0]), int(datos[1]), int(datos[2])

dinero_total = 0 
for i in range(1,w+1):
	dinero_total += k*i

dinero_a_prestar = dinero_total - n

print(dinero_a_prestar)
