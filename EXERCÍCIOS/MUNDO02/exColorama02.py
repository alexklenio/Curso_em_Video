import random
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Define as cores
cor_sucesso = Fore.GREEN
cor_erro = Fore.RED
cor_aviso = Fore.YELLOW
cor_normal = Fore.CYAN

# Título do jogo
print(f"{Style.BRIGHT}{cor_normal}--- Adivinhe o Número ---")
print("Estou pensando em um número de 1 a 10.")

# Gera um número aleatório
numero_secreto = random.randint(1, 10)
acertou = False

while not acertou:
    try:
        palpite = int(input(f"\n{Style.NORMAL}{cor_normal}Qual é o seu palpite? "))
        
        if palpite < numero_secreto:
            print(f"{cor_erro}Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print(f"{cor_erro}Muito alto! Tente novamente.")
        else:
            print(f"\n{cor_sucesso}PARABÉNS! Você acertou o número {numero_secreto}!")
            acertou = True
    except ValueError:
        print(f"{cor_aviso}Entrada inválida. Por favor, digite um número inteiro.")

# Mensagem de final de jogo
print(f"{Style.BRIGHT}{Fore.MAGENTA}Obrigado por jogar!")