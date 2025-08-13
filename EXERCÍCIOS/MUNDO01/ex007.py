#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n01= (float(input('Digite a primeira nota: ')))
n02=  (float(input('Digite a segunda nota: ')))
print('A média entre {} e {} é igual a {:.2f}'.format(n01, n02, (n01 + n02) / 2))