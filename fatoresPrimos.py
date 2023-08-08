numero = int(input('Digite um número maior do que 1: '))
fator = 2
multiplicidade = 0


while numero > 1:
    while numero % fator == 0:
        multiplicidade = multiplicidade + 1
        numero = numero / fator
    if multiplicidade > 0:
        print(f'Fator {fator}, multiplicidade = {multiplicidade}')
    fator = fator + 1
    multiplicidade = 0
