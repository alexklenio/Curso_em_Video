peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m)'))

imc = peso / (altura**2)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.0f} e você está abaixo do peso normal.')
elif imc <= 24.9:
    print(f'Seu IMC é {imc:.0f}. Parabéns você está com seu peso normal.')
elif imc <= 29.9:
    print(f'Seu IMC é {imc:.0f}. Cuidado você está acima do peso.')
elif imc <= 39.9:
    print(f'Seu IMC é {imc:.0f} e você está obeso, convên procurar ajuda de um nutricionista.')
else:
    print(f'Seu IMC é {imc:.0f} e você está muito acima do peso, é essencial o acompanhamento de um nutricionista e fazer exercícios.')