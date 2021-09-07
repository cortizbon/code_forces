n = int(input('Escriba el número de palabras: '))
lista_palabras = []
for i in range(n):
	lista_palabras.append(input('Escriba la palabra: '))

for palabra in lista_palabras:
	if len(palabra) > 10:
		print(palabra[0]+str(len(palabra)-2)+palabra[-1])
	else:
		print(palabra)


