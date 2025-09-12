numeros = []

for n in range (0, 5):
    numero = int(input(f'Informe um número para a posição {n}: '))
    numeros.append(numero)

print("-=" * 30)
print(f'Você digitou os números {numeros}')
print(f'\nO maior número digitado foi {max(numeros)} nas posições {numeros.index(max(numeros))}...')
print(f'O menor número digtado foi {min(numeros)} nas posições {numeros.index(min(numeros))}...')