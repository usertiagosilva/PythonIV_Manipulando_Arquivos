# Usando um dicionário dentro de uma lista para armazenar os cursos
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

for course in courses:
    print(f"{course['language']} - {course['category']}")
# Exibe os cursos ordenados por linguagem
        