def remove_repetidos(lista):
    lista_sem_repetidos = []
    lista.sort()
    lista_sem_repetidos.append(lista[0])
    for numero in lista:
        if numero == lista_sem_repetidos[-1]:
            del numero
        else:
            lista_sem_repetidos.append(numero)
    return lista_sem_repetidos

