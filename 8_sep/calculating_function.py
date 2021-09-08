n = int(input('Escriba el valor de n: '))

val = sum([((-1)**i)*i for i in range(1, n+1) ])

print(val)
