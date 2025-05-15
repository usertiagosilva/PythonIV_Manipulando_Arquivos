# Escrita em um arquivo CSV
# O arquivo CSV é um arquivo de texto que armazena dados em formato de tabela, onde cada linha representa um registro e cada coluna representa um campo.
import csv

name = input(" Informe o nome da linguagem de programação que deseja aprender:\n")
category = input(" Informe a categoria da linguagem:\n")

with open("dados/courses.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([name, category])
    