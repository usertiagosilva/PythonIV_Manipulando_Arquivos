import os
import csv

# Garante que o diretório exista
os.makedirs("dados", exist_ok=True)

ARQUIVO = "dados/agenda.csv"

# Adicionar um contato
def add_contact():
    name = input("Informe o nome do contato: ").strip()
    address = input("Informe o endereço do contato: ").strip()
    phone = input("Informe o telefone do contato: ").strip()

    with open(ARQUIVO, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, address, phone])
    print("Contato adicionado com sucesso!\n")

# Listar contatos
def view_contacts():
    if not os.path.exists(ARQUIVO) or os.path.getsize(ARQUIVO) == 0:
        print("Lista de contatos está vazia!\n")
        return

    print("\n** Lista de Contatos **")
    print("-" * 30)
    with open(ARQUIVO, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, 1):
            print(f"{i}. Nome: {row[0]}, Endereço: {row[1]}, Telefone: {row[2]}")
    print()

# Remover contato por nome
def delete_contact():
    name_to_delete = input("Digite o nome do contato a ser removido: ").strip()

    if not os.path.exists(ARQUIVO):
        print("Nenhum contato encontrado.\n")
        return

    updated_contacts = []
    deleted = False

    with open(ARQUIVO, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() != name_to_delete.lower():
                updated_contacts.append(row)
            else:
                deleted = True

    if deleted:
        with open(ARQUIVO, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(updated_contacts)
        print(f"Contato '{name_to_delete}' removido com sucesso!\n")
    else:
        print(f"Contato '{name_to_delete}' não encontrado.\n")
