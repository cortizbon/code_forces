k = int(input('K: '))
l = int(input('L: '))
m = int(input('M: '))
n = int(input('N: '))
d = int(input('Número de dragones: '))

lista = list(range(1,d+1))
contador = 0
for i in lista:
	if i%k==0:
		contador+=1
	elif i%l==0:
		contador+=1
	elif i%m==0:
		contador+=1
	elif i%n==0:
		contador+=1
	else:
		None

print(contador)
