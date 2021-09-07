datos = input('Participantes y cuántos avanzan: ').split()

k =int(datos[1])


scores = input('Escriba los puntajes: ').split(' ')
scores = [int(i) for i in scores]
scores.sort(reverse=True)

if max(scores)==0:
	print(0)
else:
	contador = len(scores[:k])

	for score in scores[k:]:
		if score == scores[k-1]:
			contador += 1
		else:
			None

	print(contador)
