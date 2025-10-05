def leiaDknheiro(msg):
    valido = False
    entrada = str(input(msg)).replace(',', '.').strip()
    if entrada.isalpha() or entrada == '':
        print(f'{entrada} é um preço inválido')
    else:
        valido = True
        return float(entrada)