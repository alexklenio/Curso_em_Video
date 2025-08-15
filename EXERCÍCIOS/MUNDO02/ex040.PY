nota01 = float(input('Informe  a primeira nota: '))
nota02 = float(input('Informe a segunda nota: '))
media = (nota01 + nota02) / 2

print(f'\nTirando {nota01:.1f} e {nota02:.1f}, a média do aluno é {media:.1f}')
print('')

if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O alino está REPROVADO.')
else:
    print('O aluno está APROVADO.')