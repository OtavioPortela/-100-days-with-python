lista = [1,2,3,4,5,6,7,8,9]
exibir = ""
aux = 0
for x in lista:
    aux+=1
    if aux % 3== 0:
        x = str(x)+"\n"
        exibir+=x
    else:
        exibir+=str(x)+", "

print(exibir)
