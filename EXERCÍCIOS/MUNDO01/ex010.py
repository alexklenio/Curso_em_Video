#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r, (r/5.43)))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(r, (r/6.33)))
print('Com R${:.2f} você pode comprar {:.2f}JPY'.format(r, (r/0.037)))

#como bonus proposto no video foram adicionadas as conversões para Euro e Iene
