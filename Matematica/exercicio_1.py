while True:
    print("1 - Calcular\n2 - Encerrar")
    opcao = input("Escolha umma opção: ")
    if opcao.isdigit():
        if opcao == '1':
            def calcular_expressao(expressao):
                try:
                    resultado = eval(expressao)
                    return resultado    
                except Exception as e:
                    return f"Erro ao calcular a expressão: {e}" 
            expressao = input("Digite uma expressão matemática: ")
            resultado = calcular_expressao(expressao)
            print(f"O resultado da expressão '{expressao}' é: {resultado}")      
        elif opcao == '2':
            break
    else:
        print("Digite um numero valido!")