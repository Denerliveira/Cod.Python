preco = float(input('Digite aqui o preço do produto: R$'))
print('''escolha uma opção de pagamento:
[1] A vista
[2] 2 vezes 
[3] 3 vezes
[4] 4 vezes''')
opção = int(input('escolha uma opção: '))
if opção == 1:
    total = preco - (preco * 10 / 100)
    print('o valor a vista vai de R${} para R${} com o desconto de 10%'.format(preco, total))
elif opção == 2:
    parcela = preco / 2
    print('sua compra de {} vai ser em duas parcelas iguais de {:.2f}'.format(preco, parcela))
elif opção == 3:
    juros = preco + (preco * 10 / 100)
    parcela3 = juros / 3
    print(' Sua compra de R${} vai para {:.2f}. em parcelas iguais de {:.2f}'.format(preco, juros, parcela3))
elif opção == 4:
    juros2 = preco + (preco * 15 / 100)
    parcelas4 = juros2 / 4 
    print('sua compra de R${} vai para R${:.2f} em parelas iguais de R${:.2f}'.format(preco, juros2, parcelas4))
