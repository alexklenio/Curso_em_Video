valores = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor Adicionado com sucesso!')
        valores.append(valor)

    escolha = str(input("Quer continuar? [S / N] ")).strip().upper()[0]

    if escolha == "N":
        break

print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')