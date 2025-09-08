primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("informe a razão da sua PA: "))
termo = primeiro
cont = 1

while cont <= 10:
    
    print(f"{termo} -> ", end="")
    termo += razao
    cont +=1
    
print("Fim")