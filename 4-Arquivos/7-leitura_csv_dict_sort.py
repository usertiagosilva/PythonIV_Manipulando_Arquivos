# Leitura de arquivo CSV e ordenação de dicionários
courses = []

with open("dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",", 1)  # Divide apenas na primeira vírgula
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)
# Exibe os cursos 
print(courses)

# Funções para obter a chave de ordenação
def get_category(course):
    return course["category"]

def get_language(course):
    return course["language"]


for course in sorted(courses, key=get_language):
    print(f"{course['language']} - {course['category']}")
# Exibe os cursos ordenados por linguagem
        