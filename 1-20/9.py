def ordenar(lista):
    n = len(lista)
    # Loop para controlar o número de passagens
    for i in range(n):
        troca = False
        # Loop para comparar elementos adjacentes
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Trocar os elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca = True
                # Se nenhuma troca aconteceu, a lista já está ordenada
            if not troca:
                break
            return lista

lista = [4,2,1]
lista2 =ordenar(lista)
print(lista2)