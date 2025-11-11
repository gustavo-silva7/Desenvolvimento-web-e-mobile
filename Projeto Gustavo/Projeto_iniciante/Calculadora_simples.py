while True:
    try:
        a = float(input("Digite um número: "))
        b = float(input("Digite mais um número: "))
    except ValueError:
        print("❌ Erro: Digite apenas números válidos!")
    else:
        print("\n--- OPERADORES VÁLIDOS ---")
        print("Soma = +\nSubtração = -\nMultiplicação = *\nDivisão = /")
        print()

        operador = input("Digite um operador da lista acima: ")

        if operador == '+':
            resultado = a + b
            print(f"✅ O resultado da soma é: {resultado}")

        elif operador == '-':
            resultado = a - b
            print(f"✅ O resultado da subtração é: {resultado}")

        elif operador == '*':
            resultado = a * b
            print(f"✅ O resultado da multiplicação é: {resultado}")

        elif operador == '/':
            if b == 0:
                print("❌ Erro: Divisão por zero não é permitida!")
            else:
                resultado = a / b
                print(f"✅ O resultado da divisão é: {resultado}")

        else:
            print("❌ Operador inválido!")

    # Pergunta se deseja continuar (após o resultado ou erro)
    print()
    print("1 - SIM\n0 - NÃO")
    opc = input("Deseja continuar?: ")

    if opc.isdigit() and opc == '1':
        print("\n" + "-" * 40 + "\n")
        continue
    elif opc.isdigit() and opc == '0':
        print("👋 Encerrando o programa...")
        break
    else:
        print("❌ Opção inválida! Encerrando o programa...")
        break
