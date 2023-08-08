numero = int(input('digite um número: '))
digito = 0
soma = 0
while numero > 0:
    digito = numero % 10
    soma = soma + digito
    numero = numero // 10
print(soma)
