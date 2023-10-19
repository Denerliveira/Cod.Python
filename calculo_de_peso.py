while True:
    peso = float(input('Digite aqui seu peso: '))
    altura_cm = float(input('Digite aqui sua altura em centimetros : '))
    idade = int(input(' digite aqui sua idade: '))
    sexo = input('Digite M para masculino e F para feminino: ')

    altura_metros = altura_cm / 100

    if sexo.upper() == "M":
        basal = 88.36 + (13.4 * peso) + (4.8 * altura_cm) - (5.7 * idade)
        imc = peso / (altura_metros ** 2)

        print('Sua taxa  BASAL é igual a {}'.format(basal))
        if imc < 18.5:
            print('Seu IMC é de {:.2f}. Voce esta abaixo do peso ideal'.format(imc))
        elif imc >= 18.5 and imc <= 24.9:
            print('Seu IMC é de {:.2f}. Voce esta no peso ideal'.format(imc))
        elif imc >= 25 and imc <= 29.9:
            print('Seu IMC é de {}. Você está acima do peso'.format(imc))
        elif imc >=30 and imc <= 34.9:
            print('Seu IMC é de {:.2f}. Voce esta acima do peso. Obesidade de primeiro Grau'.format(imc))
        elif imc >= 35 and imc <= 39.9:
            print('Seu IMC é de {:.2f}. Voce esta muito acima do peso. Obesidade de segundo Grau'.format(imc))
        elif imc >=40: 
            print('Seu IMC é de {:.2f}. Seu peso esta super elevado. Obesidade de Grau 3'.format(imc))
    else:
        
        basal = 447.6 + (9.2 * peso) + (3.1 * altura_cm) - (4.3 * idade)
        imc = peso / (altura_metros ** 2)

        print('Sua taxa BASAL é igual a {}'.format(basal))
        if imc < 18.5:
            print('Seu IMC é de {}. Você está abaixo do peso ideal'.format(imc))
        elif imc >= 18.5 and imc <= 24.9:
            print('Seu IMC é de {}. Você está no peso ideal'.format(imc))
        elif imc >= 25 and imc <= 29.9:
            print('Seu IMC é de {}. Você está acima do peso'.format(imc))
        elif imc >= 30 and imc <= 34.9:
            print('Seu IMC é de {}. Você está com obesidade grau I'.format(imc))
        elif imc >= 35 and imc <= 39.9:
            print('Seu IMC é de {}. Você está com obesidade grau II (severa)'.format(imc))
        elif imc >= 40:
            print('Seu IMC é de {}. Você está com obesidade grau III (mórbida)'.format(imc))
    continuar = input('Deseja calcular novamente? Digite "S" para continuar ou qualquer outra tecla para sair: ')
    if continuar.upper() != "S":
            break

    







