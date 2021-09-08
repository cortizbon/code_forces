n = input('Escriba el año: ')

n = str(int(n)+1)

while len(n)!=len(set(n)):
	n = str(int(n)+1)

print(n)
	
	
