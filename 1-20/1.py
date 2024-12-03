#Check if a number is even or odd.


def even_or_odd(number):
    try:
        if number %  2 == 0:
            return "even"
        elif number % 2 != 0:
            return "odd"
    except ValueError:
        return "Erro no calculo!!"
    
try:   
    number = int(input("report number: "))
    print(even_or_odd(number))
except:
    print("Value invalid")
