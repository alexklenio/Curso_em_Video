def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 5
    print ('~' * len(tam))
    print(f'  {msg}')
    print('~' * len(tam))


comando = ''
while True:
    titulo('SISTEMA PyHELP')
    comando = str(input('Função ou Biblioteca >')).lower()
    if comando == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')
