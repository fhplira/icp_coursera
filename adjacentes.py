numero = int(input('Digite um número inteiro: '))

adjacentesIguais = False

while numero > 0 and not adjacentesIguais:

    digito1 = numero % 10
    numero = numero // 10
    digito2 = numero % 10
    numero = numero // 10

    if digito1 == digito2:
        adjacentesIguais = True

if adjacentesIguais:
    print('sim')
else:
    print('não')
