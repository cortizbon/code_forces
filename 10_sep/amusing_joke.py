name1 = list(input('Ingrese el nombre: '))
name2 = list(input('Ingrese la dirección: '))
anagrama = list(input('Ingrese el desorden: '))

orden = name1 + name2

orden.sort()
anagrama.sort()

if ''.join(orden)==''.join(anagrama):
	print('YES')

else:
	print('NO')







