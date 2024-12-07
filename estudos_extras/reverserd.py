lista = [1,2,3,4]
var = len(lista)
listaaux = []
for x in range(len(lista)):
    if x == 0:
        aux = lista[x]
    else:
        listaaux.append(lista[-x])

listaaux.append(aux)

print(listaaux)