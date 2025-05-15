# Modulo built-in csv
# O módulo csv é uma biblioteca padrão do Python que fornece funcionalidades para ler e escrever arquivos CSV (Comma-Separated Values).
import csv 

courses = []

with open("dados/courses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Cria um leitor de dicionário
    for row in reader:
        courses.append({"language": row["language"], "category": row["category"]})  # Adiciona o dicionário à lista

# Exibe os cursos ordenados por linguagem
for course in sorted(courses, key=lambda course: course["language"]):
    print(f"{course['language']} - {course['category']}")
