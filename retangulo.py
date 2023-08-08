altura  = int(input('digite o valor da altura do retângulo: '))
largura = int(input('digite o valor da largura do retângulo: '))

if largura > altura:
    while altura > 0:
        print(largura * '#', end='\n')
        altura = altura - 1
else:
    while largura > 0:
        print(altura * '#', end='\n')
        largura = largura - 1
