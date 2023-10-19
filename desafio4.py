somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = 0 
totmulher = 0
for p in range(1 , 5):
    print('=-=-=-=-=-=-=-{}° Pessoa =-=-=-=-=-'.format(p))
    nome  = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Qual sexo? M/F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade>maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = somaidade / 4
print('A media da idade do grupo é igual a {}'.format(media))
print('O homem mais velhor tem {} de idade e se chama {}'.format(maiorhomem, nomevelho))
print('Ao todo são {} de mulhres menores de 20 anos na lista'.format(totmulher))
