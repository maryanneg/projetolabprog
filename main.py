import csv
with open('C:\\Users\\Claudinho\\Downloads\\projeto.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')
    for coluna in leitor:
        print(coluna)
