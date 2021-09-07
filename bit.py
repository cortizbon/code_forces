n = int(input('Ingrese el número: '))
x = 0
lista_operaciones = []
for i in range(n):
	lista_operaciones.append(list(input('Escriba la operación: ')))

for operacion in lista_operaciones:
	if operacion[0]=='+' or operacion[-1]=='+':
		x+=1
	elif operacion[0]=='-' or operacion[-1]=='-':
		x-=1
	else:
		None

print(x)
