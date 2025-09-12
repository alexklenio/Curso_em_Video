num=(int(input('Informe um número: ')), 
         int(input('Informe outro número: ')), 
         int(input('Mais um: ')), 
         int(input('Agora o último: ')))

print(f' Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if  3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.')
else:
    print(f'O valor 3 não foi digitado em nenuma posição.')

for n in num:
    if n % 2 == 0:
        print(n, end= " ")
    
    

