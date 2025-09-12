while  True:

    numeros =  ('zero', 'um', 'dois', 'três', 'quatro',
                'cinco', 'seis', 'sete', 'oito', 'nove',
                'dez', 'onze', 'doze', 'treze', 'catorze',
                'quinze', 'dezesseis', 'dezessete', 'dezoito',
                'dezenove','vinte')

    while True:
        num = int(input('Digite um número entre 0 e 20: '))

        if num <= 0 or num <=20:
            break
        print('Tente novamente. ', end='  ')
    print(f'Você digitou o número {numeros[num]}')

    escolha =' '
    while escolha  not in ['S', 'N']:
        escolha = str(input('Você gostaria de continua? [S / N]: ')).upper().strip()[0]
        
    if escolha == 'N':
        break