import tkinter as tk
import math

# ---------- Funções ----------
def inserir(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        limpar()
        entrada.insert(0, resultado)
    except:
        limpar()
        entrada.insert(0, "Erro")

def raiz():
    try:
        v = float(entrada.get())
        limpar()
        entrada.insert(0, math.sqrt(v))
    except:
        limpar()
        entrada.insert(0, "Erro")

def seno():
    try:
        v = float(entrada.get())
        limpar()
        entrada.insert(0, math.sin(math.radians(v)))
    except:
        limpar()
        entrada.insert(0, "Erro")

def cosseno():
    try:
        v = float(entrada.get())
        limpar()
        entrada.insert(0, math.cos(math.radians(v)))
    except:
        limpar()
        entrada.insert(0, "Erro")

def tangente():
    try:
        v = float(entrada.get())
        limpar()
        entrada.insert(0, math.tan(math.radians(v)))
    except:
        limpar()
        entrada.insert(0, "Erro")

def porcentagem():
    try:
        v = float(entrada.get())
        limpar()
        entrada.insert(0, v / 100)
    except:
        limpar()
        entrada.insert(0, "Erro")

# ---------- Janela ----------
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("450x580")
janela.configure(bg="#1e1e1e")
janela.resizable(False, False)

# ---------- Entrada ----------
entrada = tk.Entry(
    janela,
    font=("Segoe UI", 26),
    bg="#121212",
    fg="white",
    bd=0,
    justify="right"
)
entrada.pack(fill="x", padx=20, pady=20, ipady=10)

# ---------- Estilo ----------
def botao(texto, comando, cor="#2d2d2d"):
    return tk.Button(
        frame,
        text=texto,
        command=comando,
        font=("Segoe UI", 14),
        bg=cor,
        fg="white",
        activebackground="#3a3a3a",
        bd=0,
        width=6,
        height=2
    )

# ---------- Frame ----------
frame = tk.Frame(janela, bg="#1e1e1e")
frame.pack()

# ---------- Botões ----------
botoes = [
    ("C", limpar, "#d32f2f"), ("√", raiz), ("%", porcentagem), ("/", lambda: inserir("/")),
    ("7", lambda: inserir("7")), ("8", lambda: inserir("8")), ("9", lambda: inserir("9")), ("*", lambda: inserir("*")),
    ("4", lambda: inserir("4")), ("5", lambda: inserir("5")), ("6", lambda: inserir("6")), ("-", lambda: inserir("-")),
    ("1", lambda: inserir("1")), ("2", lambda: inserir("2")), ("3", lambda: inserir("3")), ("+", lambda: inserir("+")),
    ("sin", seno), ("0", lambda: inserir("0")), ("cos", cosseno), ("=", calcular, "#1976d2"),
    ("tan", tangente)
]

linha = 0
coluna = 0

for item in botoes:
    texto = item[0]
    comando = item[1]
    cor = item[2] if len(item) == 3 else "#2d2d2d"

    botao(texto, comando, cor).grid(
        row=linha,
        column=coluna,
        padx=5,
        pady=5
    )

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# ---------- Loop ----------
janela.mainloop()
