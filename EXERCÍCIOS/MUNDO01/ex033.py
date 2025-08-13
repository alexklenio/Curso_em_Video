#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num01 = int(input('Digite o primeiro valor: '))
num02 = int(input('Digite o segundo valor: '))
num03 = int(input('Digite o terceiro valor: '))

#verificando quem é menor
menor = num01
if num02 < num01 and num02 < num03:
    menor = num02
if num03 < num01 and num03 < num02:
    menor = num03

#verificando quem é maior
maior = num01
if num02 > num01 and num02 > num03:
    maior = num02
if num03 > num02 and num03 > num01:
    maior = num03

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')