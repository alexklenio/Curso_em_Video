total = totmil = menor = cont = 0
barato = " "

while True:
    prod =  str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    cont +=1
    total += preco
    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
  
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]


    if resp == "N":
        break

print("{:-^40}".format("\nFIM DO PROGRAMA"))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {totmil} produtos que custam mais de R$ 1000.00")
print(f"O produto mais barato foi {barato} que custa RR$ {menor:.2f}")