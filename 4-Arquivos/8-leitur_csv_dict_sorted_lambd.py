# Leitura de arquivo CSV e ordenação de dicionários com lambda
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


for course in sorted(courses, key=lambda course: course["language"]):
    print(f"{course['language']} - {course['category']}")
# Exibe os cursos ordenados por linguagem
        