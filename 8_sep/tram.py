n = int(input('Ingrese el número de paradas: '))

ingreso_salida = []

for _ in range(n):
	ingreso_salida.append(tuple(input('Ingresos y salidas: ').split(' ')))

ocupacion = [0]
ocupa = 0
for i, j in ingreso_salida:
	ocupa = ocupa + int(j) - int(i)
	ocupacion.append(ocupa)

print(max(ocupacion))

