tot18 = totH = totM20 = 0

print("-" * 22)
print("CADASTRE UMA PESSOA")
print("-" * 22)

while True:

    idade = int(input("INFORME A IDADE: "))
    sexo =  " "
    while sexo not in "MF":
        sexo = str(input("INFORME O SEXO [M/F]: ")).strip().upper()[0]

    if idade >= 18:
        tot18 +=1
    if sexo == "M":
        totH +=1
    if sexo == "F" and idade < 20:
        totM20 += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Gostaria de cadastrar mais uma pessoa? [S/N] ")).strip().upper()[0]

    if resp == "N":
        break

print(f"Total de pessoas commais de 18 anos: {tot18}")
print(f"Ao todo  temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos")

 