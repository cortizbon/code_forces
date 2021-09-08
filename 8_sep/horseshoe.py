datos = input('Ingrese los colores: ').split(' ')

res = len(datos) - len(set(datos))

print(res)
