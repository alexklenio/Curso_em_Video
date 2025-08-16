from colorama import Fore, Style, Back, init

init(autoreset=True)
tot = 0
num=int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c ==0:
        print(f'{Fore.YELLOW}{c}', end=' ')
        tot+=1
    else:
        print(f'{Fore.RED}{c}', end=' ')
print(f'\n O número {num} foi divisével {tot} vezes.')
if tot == 2:
    print('E por isto ele é PRIMO.')
else:
    print('E por isto ele NÃO É PRIMO.')
