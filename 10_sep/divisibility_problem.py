t = int(input('Ingrese el número de tests: '))
lista_conts = []
for _ in range(t):
	datos  = [int(i) for i in input('Ingrese los datos: ').split(' ')]
	a, b = datos[0], datos[1]
	contador = 0
	while  a%b!=0:
		a+=1
		contador+=1
	lista_conts.append(contador)
for i in lista_conts:
	print(i)
		
