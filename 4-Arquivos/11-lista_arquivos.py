# Este script lista todos os arquivos .txt e .csv em um diretório específico e compacta esses arquivos em arquivos zip separados.
import glob, os, zipfile

# 1 - Diretório de trabalho atual:
os.getcwd()

# 2 - Listar todos os arquivos .txt:
for file in glob.glob("dados/*.txt"):
    print(file)
    
# 3 - Listar todos os arquivos .csv:
for file in glob.glob("dados/*.csv"):
    print(file)
    
# 4 - Compactar arquivos .txt em um arquivo zip:
with zipfile.ZipFile("names.zip", "w") as zip:
    for file in glob.glob("dados/*.txt"):
        zip.write(file)
        
# 5 - Compactar arquivos .csv em um arquivo zip:
with zipfile.ZipFile("courses.zip", "w") as zip:
    for file in glob.glob("dados/*.csv"):
        zip.write(file)
        
# 6 - Compactar todos os arquivos:
with zipfile.ZipFile("code.zip", "w") as zip:
    for file in glob.glob("*"):
        zip.write(file)
