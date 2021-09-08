n = int(input('Número de bebidas: '))

datos = [int(i) for i in input('% de naranja: ').split(' ')]

res = sum(datos)/(n*100)

print(res*100)
