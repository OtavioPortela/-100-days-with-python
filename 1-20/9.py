def ordenar(lista):
    pos = len(lista)
    aux = lista[0]
    for x in range(pos):
        if lista[x] > aux:
            aux = lista[x]


lista = [3,2,1]
ordenar(lista)
