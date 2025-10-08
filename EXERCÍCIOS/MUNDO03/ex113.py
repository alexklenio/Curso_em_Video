def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
def leia_float(msg):
    while  True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
                print('\033[31mERRO:por favor, digite umn[umero inteiro válido.\033[m')
                continue
        except (KeyboardInterrupt):
                print('\033[31mO usuário preferiu não digitar esse número.\033[m')
                return 0
        else:
                return n


n1 = leia_int('Digite um valor: ')
n2 = leia_float('Digite um número Real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')