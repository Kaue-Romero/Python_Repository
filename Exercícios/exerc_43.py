peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (Cm) '))
IMC = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(IMC))
if IMC <= 18.5:
    print('Essa pessoa está ABAIXO DO PESO')
elif IMC <= 25:
    print('Essa pessoa está no PESO IDEAL')
elif IMC <= 30:
    print('Essa pessoa está no SOBREPESO')
elif IMC <= 40:
    print('Essa pessoa está OBESA')
else:
    print('Essa pessoa está com a OBESIDADE MÓRBIDA')
