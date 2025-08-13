#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
comp= randint(0,5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(2)

if jogador == comp:
    print('Parabéns, você conseguiu me vencer!')

elif jogador == comp+1 or jogador == comp-1:
    print('Ganhei, mas voccê quase acertou, pensei no {} e não {}!'.format(comp, jogador))

else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(comp, jogador))

#elif implementado ao ao código para adicionar mais uma condição como bônus ao desafio