from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.YELLOW +'-='*20) 
print(Style.BRIGHT +'Analisador de Triângulos')
print(Fore.YELLOW+'-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!', end='')
    if r1 == r2 == r3:
        print(Fore.GREEN+'EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print(Fore.MAGENTA+'ESCALENO')
    else:
        print(Fore.BLUE+'ISÓCELES')
else: 
    print(Fore.RED+'Os seguimentos acima NÂO PODEM FORMAR triângulo')