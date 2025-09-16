temp=[]
princ = []
mai = men = 0

while True:

    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    
    
    escolha =' '
    while escolha  not in ['S', 'N']:
        escolha = str(input('Você gostaria de continua? [S / N]: ')).upper().strip()[0]

    if escolha == 'N':
        break

print(f'-=' * 30)
print(f'Ao todo você cadastrou {len(princ)}')

print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')

print()

print(f'Omenor peso foi de {men}km. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

