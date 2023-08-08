def fatorial(n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat


numero = int(input('Digite um número inteiro: '))
while numero >= 0:
    print(fatorial(numero))
    numero = int(input('Digite um número inteiro: '))