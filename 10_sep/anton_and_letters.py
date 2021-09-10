conjunto = input('Ingrese el conjunto: ').replace('{','').replace('}','')
if conjunto=='':
	print(0)
else:
	res = len(set(conjunto.split(', ')))
	print(res)



