import time

start_time = time.time()

def fatorial(n):
    if n == 0:
        return 1
    else:
        num = 1
        for x in range(n):
            num *=(x+1)
        return f'!{n} = {num}'

number = int(input('informe the number: '))
print(fatorial(number))            

end_time = time.time()

execution_time = end_time - start_time
print(f'Tempo de execução da aplicação foi : {execution_time:.6f} segundos')