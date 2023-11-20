import model


with open('txt/cotistas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

x=0
for linha in linhas:
    if x == 0:
        x = 1
        print(linha)
    else:
        asd = linha.split(',')
        print(asd)
        model.push_shareholder(asd[1].replace('"','').strip(),'',asd[10].replace('"','').strip(),'','','',asd[0].replace('"','').strip(),asd[2].replace('"','').strip(),asd[3].replace('"','').strip(),asd[6].replace('"','')+"-"+asd[7].replace('"','').strip(),asd[4].replace('"','').strip(),asd[5].replace('"','').strip())
        """
        model.push_quote(asd[0].replace('"','').strip(),
            asd[1].replace('"','').strip(),
            asd[7].replace('"','').strip(),
            asd[2].replace('"','').strip(),
            )
        """    



#Código,Nome,Endereço,Cidade,Estado,Cep1,Cep2,FisJur,SujeitoIR,Documento,Banco,Agencia,Conta,CodFolha,Implantado,Pagamento
# Use strip() para remover caracteres de quebra de linha (\n)

"""
primeira_linha = linhas[0]  # A primeira linha é indexada como 0
print(linhas[0])
print(linhas[1])
print(linhas[2])
conteudo_como_string = ''.join(linhas)
"""




