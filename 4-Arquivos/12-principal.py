from agenda import add_contact, view_contacts, delete_contact

def main():
    while True:
        print("Agenda de Contatos")
        print("-" * 22)
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Sair")

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            add_contact()
        elif option == "2":
            view_contacts()
        elif option == "3":
            delete_contact()
        elif option == "4":
            print("Saindo da agenda de contatos...")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 4.\n")

# Executa a função principal
if __name__ == "__main__":
    main()
