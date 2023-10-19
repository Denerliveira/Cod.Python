sexo = str(input('Informe aqui seu sexo M/F: ')).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Dados invalidos, Por Favor informe seu sexo: ")).strip().upper()[0]
print('Sexo registrado com sucesso!')
                                                                                    