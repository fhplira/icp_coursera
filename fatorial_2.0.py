n = 1
fat = 1
while n > 0:
    n = int(input('Digite um número inteiro: '))
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    print(fat)
