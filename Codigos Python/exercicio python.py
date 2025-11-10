
idade = input("Digite sua idade: ")
if idade.isdigit():
    idade = int(idade)
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
else:
    print("Entrada inválida. Por favor, digite um número inteiro.")
       