number = input("Informe o numero binario: ")
value = list(number)
value = reversed(value)
aux = 0
decimal = 0
for x in value:
    x = int(x)
    if x == 0:
        aux +=1
    else:
        x =2**aux
        aux+=1
        decimal +=x
print(decimal)