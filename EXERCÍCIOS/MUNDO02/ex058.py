from random import randint

computador = randint(0,10)

print('Sou seu computador, acabei de pensar emum número ebntre 0 e 10, adivinhe!')

acertou=False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites +=1

    if jogador == computador:
        acertou  =  True
    else:
        if jogador < computador:
            print('Mais...  Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tenre mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!.')
