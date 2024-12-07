side = input("how many elements does your frame have on each side? ")
square = ''
aux = 0
for x in range(int(side)):
    aux +=1
    x = " . "
    if aux % int(side) == 0:
       x = "." +"\n"
    square+=x
print(square)


