n = int(input('Ingrese el número de personas: '))

datos = input('Ingrese las opiniones: ').split(' ')

if '1' in datos:
	print('HARD')
else:
	print('EASY')
