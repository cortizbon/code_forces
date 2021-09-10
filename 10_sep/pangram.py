n = int(input('Ingrese el largo de la palabra: '))
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
string = list(input('Ingrese el string: ').lower())

string.sort()
string2 = []
for i in string:
	if i not in string2:
		string2.append(i)

a = ''.join(string2)

if a == alfabeto:
	print('YES')

else:
	print('NO')




