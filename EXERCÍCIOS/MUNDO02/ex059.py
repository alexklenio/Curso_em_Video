from time import sleep

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
opcao = 0

while opcao != 5:
    
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")
    
    opcao = int(input("\nQual a sua opção? "))
    
    match opcao:
        case 1:
            print(f"\nA soma {n1} + {n2} é igual a {n1 + n2}.")
        case 2:
            print(f"\nA multiplicação {n1} x {n2} é igual a {n1 * n2}.")
        case 3:
            if n1 > n2:
                print(f'\n\n{n1} é maior que {n2}')
            else:
                print(f'\n{n2} é maior que {n1}')
        case 4:
            print("Informe os números novamente: \n")
            n1 = int(input('Informe o primeiro número: '))
            n2 = int(input('Informe o segundo número: '))
        case 5:
            break
        case _:  # O padrão coringa
            print("Opção inválida.")
    sleep(2)
print("Fim do programa, volte sempre!")