s = input('Escriba la suma: ').split('+')

s = [int(i) for i in s]
s.sort()
s = [str(i) for i in s]
if len(s)==1:
	print(s[0])

else:
	print('+'.join(s))


