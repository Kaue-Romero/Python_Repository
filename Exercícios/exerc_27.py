nome = str(input('Qual é o seu nome? ')).strip()
primeiro_nome = nome.split()
print('Primeiro nome {}'.format(primeiro_nome[0]))
print('Ultimo nome {}'.format(primeiro_nome[len(primeiro_nome)-1]))
