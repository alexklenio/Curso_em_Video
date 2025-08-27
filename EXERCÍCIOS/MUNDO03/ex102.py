def fatorial(n,show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: Onúmero a ser calculado.
    :param show: (opcional) Mostra ou não a conta
    :return: O valor dfatorial de um número n.
    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('\nInforme o numero o qual você quer ver o fatorial: '))
print()
print(fatorial(n, show=True))

#help(fatorial)