lista = []
pares = []
impares = []

while True:

    lista.append(int(input('Digite um número: ')))

    escolha = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if escolha == 'N':
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f' lista de impares é {impares}')