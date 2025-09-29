from time import sleep

def maior(* num):
    cont =  m = 0
    print('\nAnalizando os valores passados...')

    for value in num:
        print(f'{value} ', end='', flush = True)
        sleep(0.3)

        if cont == 0:
            m = value
        else:
            if value > m:
             m = value
        cont+=1

    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor é {m}!')


maior(1, 5, 25, 47, 6)