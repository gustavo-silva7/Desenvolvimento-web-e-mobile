while True:
    print("1 - SIM\n0 - NÃO")
    opc = input("Deseja continuar?: ")

    # Verifica se o usuário digitou um número
    if opc.isdigit():
        if opc == '1':
            try:
                a = float(input("Digite um número: "))
                b = float(input("Digite mais um número: "))
            except ValueError:
                print("Erro: Digite apenas números válidos!")
                continue  # volta ao início do laço

            print("\n--- OPERADORES VÁLIDOS ---")
            print("Soma = +\nSubtração = -\nMultiplicação = *\nDivisão = /")
            print()

            operador = input("Digite um operador da lista acima: ")

            if operador == '+':
                resultado = a + b
                print(f"O resultado da soma é: {resultado}")

            elif operador == '-':
                resultado = a - b
                print(f"O resultado da subtração é: {resultado}")

            elif operador == '*':
                resultado = a * b
                print(f"O resultado da multiplicação é: {resultado}")

            elif operador == '/':
                if b == 0:
                    print("Erro: Divisão por zero não é permitida!")
                else:
                    resultado = a / b
                    print(f"O resultado da divisão é: {resultado}")

            else:
                print("Operador inválido!")

        elif opc == '0':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida, digite 1 ou 0.")

    else:
        print("Insira uma opção válida (1 ou 0)!")
