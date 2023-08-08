altura = int(input('digite o valor da altura do retângulo: '))
largura = int(input('digite o valor da largura do retângulo: '))

if largura > altura:
    print(largura * '#', end='\n')
    altura = altura - 1
    while altura > 1:
        print(f'#{(largura - 2) * " "}#', end='\n')
        altura = altura - 1
    print(largura * '#', end='\n')
else:
    print(altura * '#', end='\n')
    largura = largura - 1
    while largura > 1:
        print(f'#{(altura - 2) * " "}#', end='\n')
        largura = largura - 1
    print(altura * '#', end='\n')