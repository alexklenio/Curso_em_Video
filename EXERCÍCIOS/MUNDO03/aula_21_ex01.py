def fatorial(num = 1):
    f = 1
    for c in range (num, 0 , -1):
        f *= c
    return f

n = int(input('\nDigite um número: '))
print(f'\nO fatorial de {n} é igual a {fatorial(n)}\n')