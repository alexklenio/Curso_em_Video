from moeda import moeda, metade, dobro, aumentar, diminuir

p = float(input('Digite o preço: R$ '))
print(f'Ametade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando em 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13, True)}')