#Decimal para binario

numero = int(input("Digite um número decimal: "))
binario = bin(numero)[2:]
print(f"O número {numero} em binário é: {binario}")

#Binario para decimal

b = input("Binário: ")
print(int(b, 2))