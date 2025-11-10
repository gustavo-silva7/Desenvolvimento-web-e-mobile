
while True: 
#Listar opções:
    print("1 - Cadastrar\n2 - Listar\n0 - Sair")
#criar a variavel e o input:
    opcao = input("Escolha: ")
#Validar se a variavel é um numero:
    if opcao.isdigit():
        if opcao == '1':
#Caso o usuaria digitar 1 inicia um função de cadastrar um nome:
#Primeiramente o codigo pede o nome:
            Listar = [ ]           
            def cadastrar_nome(nome):
#validar se o nome é valido:
                if nome and isinstance(nome,str):
#adiciona o nome na minha lista
                    Listar.append(nome.strip().title())
                    print(f"'{nome.strip().title()}' foi adicionado a lista")
                else:
                    print("Texto Invalido!")
            cadastrar_nome(nome_cadastrado)
            
            nome_cadastrado = input("Digite o nome completo: ")
        elif opcao == '2':
            print()

        elif opcao == '0':
            break
    else:
        print("Digite um numero valido!")