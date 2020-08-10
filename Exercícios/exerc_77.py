palavra = 'APRENDER', 'PROGRAMAR', \
          'LINGUAGEM', 'PYTHON', 'CURSO', \
          'GRATIS', 'ESTUDAR', 'PRATICAR', \
            'TRABALHAR', 'MERCADO', \
          'PROGRAMADOR', 'FUTURO'
for palavras in palavra:
    print(f'\nNa palavra {palavras} temos: ', end='')
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
