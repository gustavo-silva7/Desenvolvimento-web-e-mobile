import subprocess
import os

def test_wifi_password(cap_file, wordlist, bssid):
    """
    Testa senhas contra um handshake WPA2 capturado.
    
    :param cap_file: Caminho para o arquivo .cap contendo o handshake
    :param wordlist: Caminho para a wordlist de senhas
    :param bssid: BSSID do roteador (MAC address)
    """
    try:
        # Executa o aircrack-ng com os parâmetros fornecidos
        result = subprocess.run(
            ["aircrack-ng", cap_file, "-w", wordlist, "-b", bssid],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout
        if "KEY FOUND" in output:
            print("[+] Senha encontrada!")
            print(output)
        else:
            print("[-] Senha não encontrada. Tente outra wordlist.")
    except FileNotFoundError:
        print("[!] aircrack-ng não encontrado. Instale com: sudo apt install aircrack-ng")

# Exemplo de uso
if __name__ == "__main__":
    handshake_file = "/caminho/para/handshake.cap"  # Arquivo capturado via airodump-ng
    senha_wordlist = "/caminho/para/wordlist.txt"   # Ex: rockyou.txt
    router_bssid = "LIDIA VITORIA_5G"              # Substitua pelo BSSID do seu roteador

    test_wifi_password(handshake_file, senha_wordlist, router_bssid)