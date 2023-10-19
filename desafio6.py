n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opçao = 0
while opçao != 6: 
    print('''opções:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Dividir 
        [ 4 ] Maio dos dois
        [ 5 ] Novas opções
        [ 6 ] Encerrar.''')
    opçao = int(input('Escolha uma opção: '))
    if opçao ==1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2 , soma))
    elif opçao == 2:
        mult = n1 * n2
        print('O resoltado de {} * {} é igual a {}'.format(n1, n2, mult))
    elif opçao == 3:
        div = n1 /n2
        print('A divisão entre {} e {} é igual a {:.2f}'.format(n1, n2, div))
    elif opçao == 4:
        if n1 > n2:
            print('O numero {} é maior que o numero {}'.format(n1, n2))
        elif n1 ==n2:
            print('O dois numeor são de mesmo valor')
        else:
            print('O Numero {} é maior que o {}'.format(n2, n1))
    elif opçao ==5:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif opçao == 6:
        print('programa encerrado, muito obrigado e volte sempre.')
    else:
        print('Opção invalida, tenten novamente.')

    
print("fim do programa ")