import subprocess

mdb_file = "COTISTAS.mdb"
table_name = "Valores"

# Comando para listar tabelas
list_tables_command = f"mdb-tables -1 {mdb_file}"
tables = subprocess.check_output(list_tables_command, shell=True, text=True).splitlines()

if table_name in tables:
    # Comando para exportar dados da tabela
    export_command = f"mdb-export {mdb_file} {table_name}"
    data = subprocess.check_output(export_command, shell=True, text=True)
    print(data)
    nome_arquivo = "Valores.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(data)
else:
    print(f"A tabela '{table_name}' não foi encontrada no arquivo MDB.")




"""
Agencias
Bancos
Compactado
Cotistas
Creditos
IRenda
Mestre
Operadores
Rateio

Títulos
Valores
"""