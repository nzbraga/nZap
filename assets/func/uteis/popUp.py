import tkinter as tk
from tkinter import ttk, messagebox

def popUp(message):
   
    # Cria a janela principal
    popUp = tk.Tk()
    popUp.attributes("-topmost", True)
        
    # Definir o tamanho da janela
    largura_janela = 300
    altura_janela = 80

    # Obter o tamanho da tela
    largura_tela = 1920
    altura_tela = 1080

    # Calcular a posicao central
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    # Definir a geometria centralizada

    popUp.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    popUp.withdraw()  # Esconde a janela principal (nao sera mostrada)
    
    # Exibe a caixa de mensagem com a mensagem desejada
    messagebox.showinfo("Atencao", message)

def popUp_bar(message):
    popUp = tk.Toplevel()
    popUp.title("Aguarde...")
    popUp.attributes("-topmost", True)

    largura_janela = 300
    altura_janela = 100
    largura_tela = popUp.winfo_screenwidth()
    altura_tela = popUp.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    popUp.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    popUp.resizable(False, False)

    tk.Label(popUp, text=message, wraplength=280).pack(pady=10)

    progresso = ttk.Progressbar(popUp, orient="horizontal", length=250, mode="determinado")
    progresso.pack(pady=10)

    return popUp, progresso