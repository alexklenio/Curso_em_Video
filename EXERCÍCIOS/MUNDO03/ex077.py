palavras= ('estudar', 'aprender', 'ensinar', 'pyton', 'gratis', 'programacao', 'emprego', 'futuro')

for p in palavras:
    print(f'\n na palavra {p} temos ', end=" ")
    
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')