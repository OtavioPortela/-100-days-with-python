def maior_lista(lista):
    aux = 0
    for x in lista:
        if x > aux:
            aux = x
    return aux


def menor_lista(lista):
    menor = lista[0]
    for x in lista:
        if x <= menor:
            menor = x
    return menor
            
lista = [6,3,4,9,7,2,1,9, 4,6,4,23,53,32,34,6,42,64,32,4,43,2]
print(maior_lista(lista))
print(menor_lista(lista))
