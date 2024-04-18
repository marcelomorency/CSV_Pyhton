import csv

def separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora):
    tabelas_data = []
    tabelas_hora = []
    
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        # Preenche as tabelas de data e hora
        for linha in leitor_csv:
            # Verifica se a linha tem a coluna especificada
            if len(linha) > coluna_data_hora:
                data_hora = linha[coluna_data_hora].strip()  # Remove espaços em branco
                if data_hora:
                    data, hora = data_hora.split()  # Separando a data e hora
                    tabelas_data.append(data)
                    tabelas_hora.append(hora)
                else:
                    tabelas_data.append('')
                    tabelas_hora.append('')
            else:
                tabelas_data.append('')
                tabelas_hora.append('')
    
    # Escreve as tabelas de data e hora no arquivo de saída
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_saida_csv:
        escritor_csv = csv.writer(arquivo_saida_csv)
        escritor_csv.writerow(['Data', 'Hora'])
        for data, hora in zip(tabelas_data, tabelas_hora):
            escritor_csv.writerow([data, hora])

# Exemplo de uso
arquivo_entrada = 'Trabalhador CRAB Comentários + IBM - Comentários + IBM CRAB.csv'
arquivo_saida = 'dados_separadostabela.csv'
coluna_data_hora = 2  # Assumindo que a data e hora estão na terceira coluna
separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora)