n = int(input('Ingrese los niveles: '))

lx = input('Niveles de Little X: ').split(' ')
ly = input('Niveles de Little Y: ').split(' ')


niv = set(lx+ly)

if len(niv)==n:
	print('I become the guy.')

else:
	print('Oh, my keyboard!')
