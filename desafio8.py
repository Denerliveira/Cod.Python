from random import randint
from time import sleep
while True:
    itens=('Pedra', 'papel', 'tesoura')
    pc = randint(0,2)
    print('_-' * 15)
    print('''Vamos jogar Pedra, papel, e tesoura. Escolhar uma opção:
          [0] Pedra
          [1] Papel
          [2] tesoura''')
    jogador = int(input('escolha uma opção: '))
    print('_-' * 15)
    print('Pedra...')
    sleep(1)
    print('papel..')
    sleep(1)
    print('tesoura!!')
    print(f'O jogador escolheu: {itens[jogador]}')
    print(f'o Computador esolheu: {itens[pc]}')
    if pc ==0:
        if jogador ==0:
            print('Empate')
        elif jogador ==1:
            print('O jogador venceu!')
        elif jogador ==2:
            print('O Jogador perdeu!')
    elif pc ==1:
        if jogador ==0:
            print('O jogador Perde!')
        elif jogador ==1:
            print('Empate')
        elif jogador == 2:
            print('O jogador ganha!')
    elif pc == 2:
        if jogador == 0:
            print('O jogador vence')
        elif jogador == 1:
                print('O jogador Perde')
        elif jogador == 2:
            print('Empate')
    else:
        print('Opção invalida')
                    
