palabra =list(input('Escriba la palabra: '))

mayu = 0
minu = 0

for letra in palabra:
	if letra.isupper():
		mayu += 1
	else:
		minu += 1

if mayu > minu:
	print(''.join(palabra).upper())
else:
	print(''.join(palabra).lower())
