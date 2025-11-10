# ------------------------------------------------------------
# Programa: Análise de Números e Cálculos Diversos
# Autor: Gustavo Pereira da Silva
# Data: 10/11/2025
# Descrição:
#   O programa solicita um número inteiro positivo e realiza
#   diversas operações, incluindo verificação de paridade,
#   cálculo de soma, média, aprovação e fatorial.
# ------------------------------------------------------------

# ---------- Funções Utilitárias ----------

def par(numero):
    """Verifica se um número é par."""
    return numero % 2 == 0


def calcular_fatorial(n):
    """Calcula o fatorial de um número inteiro positivo."""
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial


def calcular_media(lista_numeros):
    """Retorna a média aritmética de uma lista de números."""
    if len(lista_numeros) == 0:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


def contar_positivos_negativos(lista_numeros):
    """Conta quantos números são positivos e negativos."""
    positivos = sum(1 for n in lista_numeros if n > 0)
    negativos = sum(1 for n in lista_numeros if n < 0)
    return positivos, negativos


# ---------- Programa Principal ----------

def main():
    print("=== Análise de Números ===\n")

    # Solicita o primeiro número
    while True:
        try:
            numero_inicial = int(input("Digite um número inteiro positivo: "))
            if numero_inicial <= 0:
                print("Por favor, digite um número **positivo**.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Verifica se é par ou ímpar
    if par(numero_inicial):
        print(f"O número {numero_inicial} é PAR.")
    else:
        print(f"O número {numero_inicial} é ÍMPAR.")

    # Lista para armazenar todos os números digitados
    numeros_digitados = [numero_inicial]

    # Se o número for maior que 10, pede mais 3 números
    if numero_inicial > 10:
        print("\nDigite mais 3 números inteiros:")
        novos_numeros = []
        for i in range(1, 4):
            while True:
                try:
                    n = int(input(f"Digite o {i}º número: "))
                    novos_numeros.append(n)
                    numeros_digitados.append(n)
                    break
                except ValueError:
                    print("Entrada inválida! Digite um número inteiro.")
        
        # Calcula soma e média
        soma = sum(novos_numeros)
        media = calcular_media(novos_numeros)
        print(f"\nSoma dos 3 números: {soma}")
        print(f"Média dos 3 números: {media:.2f}")

        # Verifica aprovação
        if media >= 7:
            print("Situação: Aprovado ✅")
        else:
            print("Situação: Reprovado ❌")

    # Se o número inicial ≤ 10, calcula o fatorial
    else:
        fatorial = calcular_fatorial(numero_inicial)
        print(f"\nO fatorial de {numero_inicial} é: {fatorial}")

    # Conta positivos e negativos
    positivos, negativos = contar_positivos_negativos(numeros_digitados)
    print("\n=== Estatísticas Finais ===")
    print(f"Números positivos digitados: {positivos}")
    print(f"Números negativos digitados: {negativos}")

    print("\n=== Fim do Programa ===")


# ---------- Execução do Programa ----------
if __name__ == "__main__":
    main()



# Explicação Linha por Linha
# Cabeçalho com comentários: explica o objetivo do programa, autor e descrição geral.
# Função par(numero): verifica se o número é par (retorna True) ou ímpar (retorna False).
# Função calcular_fatorial(n): calcula o fatorial de um número usando um laço for.
# Função calcular_media(lista_numeros): calcula a média de uma lista de números; retorna 0 se a lista estiver vazia.
# Função contar_positivos_negativos(lista_numeros): conta quantos números positivos e negativos foram digitados.
# Função main(): ponto de partida do programa; pede um número inteiro positivo e valida a entrada.
# Verificação par/ímpar: usa par para informar se o número é par ou ímpar.
# Se número inicial > 10: pede mais 3 números, calcula soma e média, e imprime se o usuário está "Aprovado" (média >=7) ou "Reprovado".
# Se número inicial <= 10: calcula e mostra o fatorial do número.
# Estatísticas finais: usa contar_positivos_negativos para mostrar quantos números positivos e negativos foram digitados, considerando todos os números inseridos.
# Final do programa: imprime mensagem de encerramento.
