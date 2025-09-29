def title(msg):

    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


def soma(a, b):
    s = a + b
    print(s)

def sub(a, b):
    s = a - b
    print(s)

def div(a, b):
    d = a / b
    print(d)    

def mult(a, b):
    m = a * b
    print(m)




title(" SISTEMA DE ALUNOS ")

title(" TESTANDO TÍTULO ")

title(" CURSO DE PYTHON ")

soma(4, 5)
sub(10, 8)
div(4, 2)
mult(2, 3)


#exemplo de função reebendo uma lista
def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,3,9,1,0,2]

dobra(valores)
print(valores)

#exemplo de função com desempacotamento
def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma2(5,2)
soma2(2,9,4)