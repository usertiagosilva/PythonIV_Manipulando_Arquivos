courses = []

with open("dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line or ',' not in line:
            continue  # Ignora linhas vazias ou mal formatadas
        language, category = line.split(",", 1) # Divide apenas na primeira vírgula
        courses.append(f"{language.strip()} - {category.strip()}")

for course in sorted(courses):
    print(course)
