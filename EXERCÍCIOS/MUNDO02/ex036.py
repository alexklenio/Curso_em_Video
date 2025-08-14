#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))

parcela = valor / (anos * 12)
limite = salario * 30 / 100

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcela:.2f}')

if parcela > limite:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')