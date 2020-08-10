def notas(*n, sit=False):
    """
    -> Analisar notas de alunos
    :param n: Lista de notas
    :param sit: Mostrar situação do aluno de acordo com a média (opicional)
    :return: Retorna uma lista de valores
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] <= 4:
            r['Situação'] = 'Reprovado'
        elif r['Média'] <= 6:
            r['Situação'] = 'Recuperação'
        else:
            r['Situação'] = 'Aprovado'
    return r


resp = notas(3, sit=True)
print(resp)
