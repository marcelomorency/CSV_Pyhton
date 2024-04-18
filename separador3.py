import csv

def separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora):
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_csv, open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_saida_csv:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(arquivo_saida_csv)

        # Escreva o cabeçalho no arquivo de saída
        cabecalho = next(leitor_csv)
        cabecalho.append('Data')
        cabecalho.append('Hora')
        escritor_csv.writerow(cabecalho)

        for linha in leitor_csv:
            # Verifica se a linha tem a coluna especificada
            if len(linha) > coluna_data_hora:
                data_hora = linha[coluna_data_hora].strip()  # Remove espaços em branco
                if data_hora:
                    data, hora = data_hora.split()  # Separando a data e hora
                    linha.append(data)
                    linha.append(hora)
                else:
                    linha.append('')
                    linha.append('')
            else:
                linha.append('')
                linha.append('')
            escritor_csv.writerow(linha)

# Exemplo de uso
arquivo_entrada = 'Trabalhador CRAB Comentários + IBM - Comentários + IBM CRAB.csv'
arquivo_saida = 'dados_separados2.csv'
coluna_data_hora = 2  # Assumindo que a data e hora estão na terceira coluna
separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora)