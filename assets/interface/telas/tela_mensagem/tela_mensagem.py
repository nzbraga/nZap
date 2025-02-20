import tkinter as tk


def tela_mensagem(raiz_principal):

    enviar_raiz = tk.Frame(raiz_principal) 
    tk.Label(enviar_raiz, text="Mensagens", font=("Arial", 14)).pack(pady=5)
   
    return enviar_raiz