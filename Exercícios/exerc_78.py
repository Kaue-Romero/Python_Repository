n = []
maior = menor = 0
for count in range(0, 5):
    n.append(int(input(f'Digite um número para a posição {count}: ')))
    if count == 0:
        maior = menor = n[count]
    else:
        if n[count] > maior:
            maior = n[count]
        if n[count] < menor:
            menor = n[count]
print(f'Você digitou os valores: {n}')
print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(n):
    if v == maior:
        print(f'{i}...')
print(f'E o menor valor foi {menor} na posição ', end='')
for y, h in enumerate(n):
    if h == menor:
        print(f'{y}...', end='')
