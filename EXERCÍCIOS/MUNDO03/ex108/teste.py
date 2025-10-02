from moeda import moeda,metade, dobro, aumentar

p = float(input('Digite o preço: R$ '))
print(f'Ametade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando em 10%, temos {moeda(aumentar(p, 10))}')