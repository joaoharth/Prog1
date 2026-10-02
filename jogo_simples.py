import json
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


with open("//Servidor/Documentos/Contabilidade - Fiscal/Lucas/PESSOAL/IFRS/PROG 1/baralho_bebidas_corrigido.json", "r", encoding="utf-8") as f:
    cartas = json.load(f)


def comparar(atributo):
    global carta_jogador, carta_pc

    if carta_jogador["trunfo"] == "sim":
        resultado = "Você venceu (SUPER TRUNFO!)"
    elif carta_pc["trunfo"] == "sim":
        resultado = "Computador venceu (SUPER TRUNFO!)"
    else:
        val_jogador = carta_jogador[atributo]
        val_pc = carta_pc[atributo]


        if atributo in ["acidez", "ano_criacao"]:
            if val_jogador < val_pc:
                resultado = "Você venceu"
            elif val_jogador > val_pc:
                resultado = "Computador venceu"
            else:
                resultado = "Empate"
        else:
            if val_jogador > val_pc:
                resultado = "Você venceu"
            elif val_jogador < val_pc:
                resultado = "Computador venceu"
            else:
                resultado = "Empate"

    
    info = f"""\
Resultado: {resultado}

Carta do Computador: {carta_pc['nome']}
- Teor Alcoólico: {carta_pc['teor_alcoolico']}%
- Acidez: {carta_pc['acidez']}
- Ano de Criação: {carta_pc['ano_criacao']}
- Preço: R$ {carta_pc['preco']:.2f}
"""
    messagebox.showinfo("Resultado", info)


def mostrar_carta():
    global carta_jogador, carta_pc, img

    carta_jogador = random.choice(cartas)
    carta_pc = random.choice(cartas)
    while carta_pc == carta_jogador:
        carta_pc = random.choice(cartas)

    for widget in frame.winfo_children():
        widget.destroy()

    
    tk.Label(frame, text=carta_jogador["nome"], font=("Helvetica", 16, "bold")).pack(pady=5)

    
    try:
        imagem = Image.open(f"//Servidor/Documentos/Contabilidade - Fiscal/Lucas/PESSOAL/IFRS/PROG 1/imagens/{carta_jogador['imagem']}")
        imagem = imagem.resize((250, 250))
        img = ImageTk.PhotoImage(imagem)
        tk.Label(frame, image=img).pack(pady=5)
    except:
        tk.Label(frame, text="[Imagem não encontrada]", fg="red").pack(pady=5)

    
    tk.Label(frame, text=f"Teor Alcoólico: {carta_jogador['teor_alcoolico']}%", font=("Arial", 12)).pack()
    tk.Label(frame, text=f"Acidez: {carta_jogador['acidez']}", font=("Arial", 12)).pack()
    tk.Label(frame, text=f"Ano de Criação: {carta_jogador['ano_criacao']}", font=("Arial", 12)).pack()
    tk.Label(frame, text=f"Preço: R$ {carta_jogador['preco']:.2f}", font=("Arial", 12)).pack()

    
    for atributo in ["teor_alcoolico", "acidez", "ano_criacao", "preco"]:
        nome = atributo.replace("_", " ").title()
        botao = tk.Button(frame, text=f"Comparar: {nome}",
                          command=lambda a=atributo: comparar(a),
                          bg="#4CAF50", fg="white", font=("Arial", 11), width=25)
        botao.pack(pady=4)


root = tk.Tk()
root.title("Super Trunfo IFRS - Bebidas")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()


botao_nova = tk.Button(root, text="Sortear Nova Carta", command=mostrar_carta,
                       bg="#555", fg="white", font=("Arial", 10))
botao_nova.pack(pady=10)

mostrar_carta()
root.mainloop()
