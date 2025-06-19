while True:
        try:
            peso = float(input('Qual o seu peso? (kg) '))
            if peso <= 0:
                print('O peso deve ser maior que zero. Tente novamente.\n')
                continue
            break
        except ValueError:
            print('Entrada inválida! Digite um número válido para o peso.\n')

while True:
        try:
            altura = float(input('Qual a sua altura? (m) '))
            if altura <= 0:
                print('A altura deve ser maior que zero. Tente novamente.\n')
                continue
            break
        except ValueError:
            print('Entrada inválida! Digite um número válido para a altura.\n')
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu IMC é {imc:.2f}.')
    print('Classificação: O Abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'O seu IMC é {imc:.2f}.')
    print('Classificação: Peso normal.')
elif imc >= 25 and imc <= 29.9:
    print(f'O seu IMC é {imc:.2f}.')
    print('Classificação: Sobrepeso.')
elif imc >= 30 and imc <= 34.9:
    print(f'O seu IMC é {imc:.2f}.')
    print('Classificação: Obesidade grau 1.')
elif imc >= 35 and imc <= 39.9:
    print(f'O seu IMC é {imc:.2f}.')
    print('Classificação: Obesidade grau 2.')
elif imc >= 40:
    print(f'O seu IMC é {imc:.2f}.')
    print('Classificação: Obesidade grau 3.')
else:
    print('Entrada invalidada. ')
