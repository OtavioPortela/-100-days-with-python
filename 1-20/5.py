def reverser(palavra):
    lista = palavra
    listaaux = []
    for x in range(len(lista)):
        if x == 0:
            aux = lista[x]
        else:
            listaaux.append(lista[-x])

    listaaux.append(aux)

    return listaaux



palavra = input('Informe a palavra para verificar se e um palindromo: ')
verif = reverser(palavra)

if list(palavra) == verif:
    print("E um palindromo !!!")
else:
    print("Nao e um palindromo!!")
