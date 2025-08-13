#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidde atual do carro? '))
limite = 80
multa=(vel-80)*7

if vel > 80:
    print('MULTADO!, Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
else:
    print('{}km/h é uma velocidade segura, você não foi multado.'.format(vel))

print('Tenha um bom dia e dirija com segurança!')
