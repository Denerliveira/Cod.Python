soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor'.format(c)))
    if num % 2 ==0:
        soma = soma + num
        cont = cont + 1
print('Voce informou {} valores pares e a soma entre eles é igal a {} '.format(cont, soma))

