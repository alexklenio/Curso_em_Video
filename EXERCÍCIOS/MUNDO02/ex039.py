from datetime import date

atual = date.today().year
nasc = int(input('\nInforme seu ano de nascimento: '))
idade = atual - nasc

print(f'\nQuem nasceu em {nasc} tem {idade} anos em {atual}')

if idade < 18:
    saldo = 18-idade
    print(f'\nVocê ainda não tem 18 anos. Ainda faltam {saldo} anos para se alistar')
    ano = atual + saldo
    print(f'Ainda faltam {ano} anos para o seu alistamento')
    print('')

elif idade > 18:
    saldo = idade - 18
    print(f'\nVocê ja deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'\nSeu alistamento foi em {ano}')
    print('')
else:
    print('\nVocê tem que se alistar IMEDIATAMENTE')
    print('')