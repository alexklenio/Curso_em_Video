#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em Graus Celcius: '))
far = ((9 * temp) / 5 + 32)

print('A tempetarura de {}C corresponde a {}F!'.format(temp, far))