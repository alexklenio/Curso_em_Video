soma = 0
cont = 1


while True:
    numero = int(input("Digite o número 999 para parar: "))

    if numero == 999:
        break
    else:
        soma += numero
        cont+=1

print(f"\nVocê informou {cont} números e a soma de todos eles é igual a {soma}")