import tkinter as tk
from tkinter import ttk, messagebox

from assets.func.sessao.sessao import sessao_id

def criar_tela_agendadas(raiz_principal):

    frame_agendadas = tk.Frame(raiz_principal)

# Remetente
    tk.Label(frame_agendadas, text="Numero de confirmação:", font=("Arial", 8)).pack(pady=(20, 5), padx=5)
  
    # Ajusta a janela ao conteúdo
    raiz_principal.update_idletasks()
    raiz_principal.geometry("")

    return frame_agendadas
