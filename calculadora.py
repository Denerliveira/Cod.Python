num = int(input('Escolha um numero para saber sua taboada: '))
for c in range(1, 11):
    print( '{} x {:2} = {}'.format(num, c, num*c))