x = int(input("number"))
for i in range(x+1):
    if x % i == 0 and i != 1 and i != x and i != 0:
        print("Primo")
            
        