print("Gerador de PA")
print("-=" * 15)
    
primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("informe a razão da sua PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
  
while mais != 0:  
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont +=1
        
    print("PAUSA")
    mais = int(input("Quantos termos você quermostrar a mais?: "))
            
print("\nFIM")
print(f"Progressão finalizada com o total de {total} termos.")