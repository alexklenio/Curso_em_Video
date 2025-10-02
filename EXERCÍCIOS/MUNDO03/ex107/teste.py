import moeda

p = float(input('Digite o preço: R$ '))
print(f'Ametade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando em 10%, temos R$ {moeda.aumentar(p, 10)}')