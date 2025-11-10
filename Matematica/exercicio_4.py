# Converter número de base 8 para base 10

# Pede o número em base 8
numero_octal = input("Digite um número em base 8: ")

# Converte para base 10 usando int()
numero_decimal = int(numero_octal, 8)

# Mostra o resultado
print(f"O número {numero_octal} em base 8 equivale a {numero_decimal} em base 10.")


# Converter número de base 10 para base 8

# Pede o número em base 10
numero_decimal = int(input("Digite um número em base 10: "))

# Converte para base 8 usando a função oct()
numero_octal = oct(numero_decimal)[2:]  # [2:] remove o prefixo '0o'

# Mostra o resultado
print(f"O número {numero_decimal} em base 10 equivale a {numero_octal} em base 8.")
