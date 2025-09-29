from time import sleep

def lin(msg):
    print('-=' * 35)
    print(msg)


def contador():
    lin('  \nContagem de 1 até 10 de 1 em 1:  ')
    
    for n in range(1,11):
        print(n, end=' ', flush=True)
        sleep(0.5)

    print()
    print()

    lin('  \nContagem de 10 até 0 de 2 em 2:  ')
    
    for n in range(10, -1, -2):
        print(n, end=' ', flush=True)
        sleep(0.5)   

    print()
    print()

    lin('  \nAgora é a sua vez de personalizar a contagem:  ')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    lin(f'Contagem de {i} até {f} de {p} em {p}:')
    for n in range(i, f+1, p):
        
        print(n, end=' ', flush=True)
        sleep(0.5) 

contador()