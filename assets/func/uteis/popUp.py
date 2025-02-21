import tkinter as tk
from tkinter import messagebox

def popUp(message):
   
    # Cria a janela principal
    popUp = tk.Tk()
    popUp.attributes("-topmost", True)
        
    # Definir o tamanho da janela
    largura_janela = 400
    altura_janela = 100

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

    label_texto = tk.Label(popUp, text=message, wraplength=280)
    label_texto.pack(pady=10)

    spinner = tk.Label(popUp, text=".", font=("Arial", 30))
    spinner.pack(pady=10)

    def animar_pontos():
        estados = [".", "..", "...", ""]  # Alterna entre os pontos
        idx = 0

        def mudar_estado():
            nonlocal idx
            spinner.config(text=estados[idx])
            idx = (idx + 1) % len(estados)
            popUp.after(500, mudar_estado)  # Muda a cada 500ms

        mudar_estado()  # Inicia a animação

    animar_pontos()

    return popUp
