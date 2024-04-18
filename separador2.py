import csv

def separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora):
    with open(arquivo_entrada, 'r') as arquivo_csv, open(arquivo_saida, 'w', newline='') as arquivo_saida_csv:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(arquivo_saida_csv)

        # Escreva o cabeçalho no arquivo de saída
        cabecalho = next(leitor_csv)
        cabecalho.append('Data')
        cabecalho.append('Hora')
        escritor_csv.writerow(cabecalho)

        for linha in leitor_csv:
            data_hora = linha[1]  # Acessa a coluna especificada
            data, hora = data_hora.split()  # Separando a data e hora
            linha.append(data)
            linha.append(hora)
            escritor_csv.writerow(linha)

# Exemplo de uso
arquivo_entrada = 'Trabalhador CRAB Comentários + IBM - Comentários + IBM CRAB.csv'
arquivo_saida = 'dados_separados.csv'
coluna_data_hora = 2  # Assumindo que a data e hora estão na terceira coluna
separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora)