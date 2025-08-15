
print('\033[33m-=\033[m'*20) 
print('Analisador de Triângulos')
print('\033[33m-=\033[m'*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else: 
    print('Os seguimentos acima NÂO PODEM FORMAR triêngulo')