expr = str(input('Digite a expresão: '))
pilha = []
for simb in expr == '(':
    if len(pulha) > 0:
        pilha.pop()
    else:
        pilha.append(')')
        break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão estáerada!.')