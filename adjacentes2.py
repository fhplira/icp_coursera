n = int(input('Digite um número inteiro: '))

adjacentesIguais = False

while n > 0 and not adjacentesIguais:
    n1 = n % 10
    n = n // 10
    n2 = n % 10

    if n1 == n2:
        adjacentesIguais = True

if adjacentesIguais:
    print('sim')
else:
    print('não')
