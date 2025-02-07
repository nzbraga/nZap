import tkinter as tk


def tela_contatos(raiz_principal):
   
    frame_inicial = tk.Frame(raiz_principal, bg="white")
    tk.Label(frame_inicial, text="Tela de Contatos", font=("Arial", 14)).pack(expand=True)


    return frame_inicial
