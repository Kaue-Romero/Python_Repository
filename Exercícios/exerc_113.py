def leiaInt(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[:31mERRO: \"{entrada}\" não é um número válido!\033[m')
        else:
            válido = True
            return int(entrada)


def leiaFloat(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[:31mERRO: \"{entrada}\" não é um número válido!\033[m')
        else:
            válido = True
            return float(entrada)


print(
    f'O valor inteiro foi {leiaInt("Digite um número inteiro: ")} e o real foi {leiaFloat("Digite um número real: ")}')
