tab = int(input('Digite um número para ver a sua tabuada: '))
cont = 1

print(f'\nVocê escolheu a tabuada de {tab}!')
print('')
for c in range(1, 11):
    print(f'{tab} x {cont:2} = {tab * cont}')
    cont += 1
print('')
print('Bons estudos!')
print('')