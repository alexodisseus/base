import model


with open('txt/titulos.txt', 'r') as arquivo:
    linhas = arquivo.readlines()


"""
linha = linhas[1]


model.push_quote(linha)
"""

x=0
for linha in linhas:
    if x == 0:
        x = 1
        print(linha)
    else:
        asd = linha.split(',')
        print(asd)
        
        model.push_quote(asd )


