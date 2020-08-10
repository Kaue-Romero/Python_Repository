vel = float(input('Qual a velocidade do carro: '))
multa = (vel - 80) * 7
print('Você esta dentro do limite de velocidade'if vel <= 80 else 'você deve pagar R${:.2f} de multa'.format(multa))
