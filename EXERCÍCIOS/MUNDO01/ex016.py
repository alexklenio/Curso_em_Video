# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção I

from math import trunc

num = float(input('Digite um número: '))

print('Onúmero {} tem a parte inteira {}.'.format(num, trunc(num)))
