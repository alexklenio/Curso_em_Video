from time import sleep

def lin(msg):
    print('-=' * 35)
    print(msg)
    print()

def contador(i, f, p):
    lin(f'Contagem de {i} até {f} de {p} em {p}')
    
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p 
            sleep(0.5)
        print('FIM!\n')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM!\n')

    
contador(0, 100, 10)
contador(10, 0, 2)

lin('Agora é a sua vez de personalizar a contagem! ')
ini = int(input('Inpicio: '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))

contador(ini, fim, pas)