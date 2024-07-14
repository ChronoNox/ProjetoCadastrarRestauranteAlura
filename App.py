Restaurantes = []
RestauranteASerAlterado = " "
op = " "

print("""
███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗██╗░█████╗░██╗░░░░░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔══██╗██║░░░░░
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░██║███████║██║░░░░░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██╔══██║██║░░░░░
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝██║██║░░██║███████╗
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚══════╝
\n""")

def Opcoes():
    op = ""
    while op not in ("1", "2", "3", "4"):
        print("1. Cadastrar restaurante:")
        print("2. Listar restaurante:")
        print("3. Ativar restaurante:")
        print("4. Sair\n")
        op = input("Escolha uma opção: \n")
        if op not in ("1", "2", "3", "4"):
            print("Por favor, escolha uma das opções disponíveis\n")
    return op

op = Opcoes()

while op != "4":
    if op == "1":
        Restaurantes.append ([input("Insira o nome do restaurante que pretende cadastrar: "), "Inativo"])
        op = Opcoes()    
    if op == "2":
        print("Restaurantes cadastrados:")
        for restaurante in Restaurantes:
            print(f"- {restaurante[0]}: {restaurante[1]}")
        op = Opcoes()
    if op == "3":
        restaurante_ativo = input("Qual restaurante deseja ativar? ")
        for restaurante in Restaurantes:
               if restaurante[0] == restaurante_ativo:
                 restaurante[1] = "Ativo"
                 print(f"Restaurante '{restaurante_ativo}' ativado.")
        op = Opcoes()

print("Saindo...")