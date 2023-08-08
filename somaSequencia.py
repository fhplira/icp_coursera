sequencia = int(input('Qual a quantidade de números a serem somados: '))
quantidade = 0
soma = 0
valor = 0
while quantidade < sequencia:
    valor = int(input('Digite um valor a ser somado: '))
    soma = soma + valor
    quantidade = quantidade + 1
print(f'A soma dos valores digitados é {soma}')
