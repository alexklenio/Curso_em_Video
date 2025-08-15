'''
Instalação:
pip install colorama
'''

#importa o colorama
from colorama import Fore, Back, Style, init

# Inicializa o Colorama com autoreset
init(autoreset=True)

print(f"{Fore.CYAN}--- Sistema de Login ---")

# Mensagem de sucesso (verde)
print(f"{Fore.GREEN}Login efetuado com sucesso!")

# Mensagem de aviso (amarelo)
print(f"{Fore.YELLOW}Atenção: A sua senha expira em 3 dias.")

# Mensagem de erro (vermelho com fundo amarelo)
print(f"{Fore.RED + Back.YELLOW + Style.BRIGHT}ERRO: Falha ao conectar com o banco de dados!")

# Mensagem normal com estilo negrito
print(f"{Style.BRIGHT}Bem-vindo, Administrador!")

# Mensagem para o usuário aguardar
print(f"{Fore.MAGENTA}Aguardando novas operações...")
