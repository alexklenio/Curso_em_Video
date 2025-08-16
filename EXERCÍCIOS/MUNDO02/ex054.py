from datetime import date
maior=0
menor=0
ano = date.today().year
cont = 0

for c in range(1, 8):
    nascimento = int(input(f'\n Em que ano a {cont+1}º pessoa nasceu? '))
    if (ano - nascimento) >= 18:
        maior +=1
        cont +=1
        
    else:
        menor +=1
        cont +=1

print(f'\nAo todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
print('')