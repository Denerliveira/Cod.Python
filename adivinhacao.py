from random import randint
pc = randint(0, 10)
print('Vamos jogar!, adivinhe o nuemro que eu pensei entre 0 e 10')
print('Sera que vc consegue acertar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Um pouco mais, tente de novo')
        elif jogador > pc:
            print('um pouco menos, tente de novo.')
print('Acertou com {} tentativas,'.format(palpite))

