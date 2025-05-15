name = input("Digite o seu nome:\n")

# Arquivos:
# 1 - opção w - write - cria o arquivo e sobrescreve o conteúdo
# 2 - opção a - append - cria o arquivo e adiciona o conteúdo no final do arquivo
# 3 - opção x - exclusive - cria o arquivo e não sobrescreve o conteúdo, caso o arquivo já exista, gera um erro
# 4 - opção r - read - lê o arquivo, não cria o arquivo, não sobrescreve o conteúdo, caso o arquivo não exista, gera um erro
# 5 - opção r+ - read and write - lê o arquivo e sobrescreve o conteúdo, caso o arquivo não exista, gera um erro
# 6 - opção a+ - append and read - lê o arquivo e adiciona o conteúdo no final do arquivo, caso o arquivo não exista, cria o arquivo
# 7 - opção w+ - write and read - lê o arquivo e sobrescreve o conteúdo, caso o arquivo não exista, cria o arquivo

# Alternativa 1
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Alternativa 2 - with open
with open("dados/names.txt", "a") as file:
    file.write(f"{name}\n")
