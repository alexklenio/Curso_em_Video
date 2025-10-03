def aumentar(preco, taxa, formato=False):
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(preco,taxa, formato=False):
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)

def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print("-"*35)
    print("RESUMO DO VALOR".center(35))
    print("-"*35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print("-"*35)