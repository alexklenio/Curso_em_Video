from random import randint
from time import sleep

numeros = list()
soma_pares = cont = 0

def pares(numeros):
    global cont
    global soma_pares

    while cont < 5:
        num = randint(1, 10)
        if num in numeros:
            pass
        else:
            numeros.append(num)
            cont += 1

    print('Sorteando 5 valores: ', end='')

    for value in numeros:
        if value % 2 == 0:
            soma_pares += value

        print(f'{value} ', end='', flush=True)
        sleep(0.5)

    print('PRONTO!')
    print(f'Somando os valores pares de {numeros}, temos {soma_pares}')
    
 