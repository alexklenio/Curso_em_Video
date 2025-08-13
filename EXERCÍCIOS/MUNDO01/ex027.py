#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()

print('Seu primeiro nome é {}'.format(nomes[0]))
print('Seu ultimo nome é {}'.format(nomes[len(nomes)-1]))