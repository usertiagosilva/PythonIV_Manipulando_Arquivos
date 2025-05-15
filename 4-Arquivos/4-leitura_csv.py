# Ler um arquivo CSV e imprimir os dados
with open("dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        # row = line.strip().split(",")
        # print(row[0], row[1])
        # Desempacotando a linha em duas variáveis
        language, category = line.strip().split(",")
        print(f"Linguagem: {language} -- Categoria: {category}")