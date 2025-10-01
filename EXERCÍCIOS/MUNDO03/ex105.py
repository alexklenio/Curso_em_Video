def notas(*n, sit = False):
    """
    -> Função para analizar notas e situaçõe devários alunos.
    :param n: uma ou mais notas  dos alunos (aceita várias)
    :param sit: valor  oprcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação  da turma.
    """


    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


resp = notas(5.5, 2.5, 8.5, sit = True)
print(resp)

help(notas)