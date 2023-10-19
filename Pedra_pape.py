while True: 
    from random import randint
    itens = ('pedra', 'papel', ' tesoura')
    computador = randint(0,2)
    print('O computador escolheu {}'.format(itens[computador]))
    print("-=-" * 12)
    print('''opções:
    [0] Pedra
    [1] Papel 
    [2] Tesolra''')
    print('-=-' * 12)
    jogador = int(input('escolha uma das opções: '))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('O computador escolheu {}'.format(itens[computador]))
    if computador == 0: 
        if jogador == 0:
            print('Voces emparatam o jogo.')
        elif jogador == 1:
            print('o Jogador vence a partida')
        elif jogador == 2:
            print('O Computador vence a partida')
        else:
            print('Opção invalida, tente novamente')

    elif computador == 1:
        if jogador == 0:
            print('O Jogador perde a partida')
        elif jogador == 1:
            print('Voces empataram o jogo')
        elif jogador == 2:
            print('O Jogador vence a partida')
        else:
            print('Opção invalida, tente novamente')
    elif computador == 2:
        if jogador == 0:
            print ('O Jogador vence a partida')
        elif jogador == 1:
            print('O Computador vence a partida!')
        elif jogador == 2:
            print('voces empataram')
        else:
            print('Opção invalida, tente novamente')
    continuar = input('Deseja calcular novamente? Digite "S" para continuar ou qualquer outra tecla para sair: ')
    if continuar.upper() != "S":
            break       



