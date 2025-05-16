import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def popUp(message, title="Atencao"):
   
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
    messagebox.showinfo(title, message)



def carregar():
    """Simula uma tarefa longa em uma thread separada."""
    time.sleep(5)  # Simula um processo demorado (5 segundos)
    loading_window.after(0, loading_window.destroy)  # Fecha o pop-up na thread principal

def show_loading():
    global loading_window
    loading_window = tk.Toplevel(root)
    loading_window.title("Carregando...")
    loading_window.geometry("250x100")
    loading_window.resizable(False, False)
    loading_window.grab_set()  # Bloqueia interação com a janela principal

    tk.Label(loading_window, text="Aguarde...", font=("Arial", 12)).pack(pady=10)

    progress = ttk.Progressbar(loading_window, mode="indeterminate", length=200)
    progress.pack(pady=5)
    progress.start()

    # Inicia a tarefa longa em uma thread separada
    thread = threading.Thread(target=carregar, daemon=True)
    thread.start()


