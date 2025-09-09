from random import randint
v = 0
while True:
    play = int(input("Informe um número inteiro: "))
    comp = randint(1,10)
    total = play + comp
    tipo = " "
    
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    
    print(f"Você jogou {play} e o computador {comp}. Total de {total} ", end=" ")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")

    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU")
            v += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")

print(f"GAME OVER! Você venceu {v} vezes.")