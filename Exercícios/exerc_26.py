frase = str(input('Digite um frase: ')).lower().strip()
count = frase.count('a')
começo = frase.find('a')
final = frase.rfind('a')
print('Sua frase tem {} a q começam na posição {} e terminam na posição {}'.format(count, começo + 1, final + 1))