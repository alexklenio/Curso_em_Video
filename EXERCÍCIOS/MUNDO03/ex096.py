def area ():
    
    print('\nCOntrole de terrenos')
    print('---------------------\n')
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    
    a = l * c
    print(f'\nA área de um terreno {l}x{c} é de {a}m²\n')


area()