#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num01 = int(input('Informe o primeiro número: '))
num02 = int(input('Informe o segundo número: '))

if num01 > num02:
    print('O primeiro número é maior')
elif num01 < num02:
    print('O segundo número é maior')
else:
    print('não existe valor maior, os dois são iguais')