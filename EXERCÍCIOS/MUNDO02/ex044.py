print(f'{" LOJAS GUANABARA ":=^40}')

preco = float(input('\nPreço das compras: R$'))
print('''Formas de pagamento
[ 1 ] à vista em dinheiro / PIX
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('QUal é a opção? '))

if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao ==  3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R$ {parcela:.2f} COM JUROS')
else:
    total = preco
    print('Opção INVÁLIDA de pagamento, tente novamente')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final')