elemento_da_lista = 1
lista = []
while elemento_da_lista != 0:
    elemento_da_lista = int(input('digite um número: '))
    lista.append(elemento_da_lista)

sorted(lista)
del lista[-1]
lista.reverse()

for elemento in lista:
    print(elemento)
