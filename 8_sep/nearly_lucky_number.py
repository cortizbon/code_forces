n = list(input('Ingrese el número: '))

contador = 0

for i in n:
	if int(i)==4 or int(i)==7:
		contador+=1

if contador!=0 and (contador%4==0 or contador%7==0):
	print('YES')
else:
	print('NO')


