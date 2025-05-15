# Resolução exercicio 1

# Função para ler as primeiras n linhas de um arquivo
def file_read_lines(file_name, n):
   from itertools import islice
   with open(file_name, 'r', encoding='utf-8') as file:
       for line in islice(file, n):
           print(line.strip())
           
# Teste da função file_read_lines
file_read_lines("dados/text.txt", 5)
