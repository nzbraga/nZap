import tkinter as tk
from tkinter import ttk, messagebox

from assets.func.sessao.sessao import sessao_nome

remetente = None
primeira_hora = None
ultima_hora = None
intervalo = None

def mostrar_ajuda(ajuda):
    if ajuda == "remetente":
        messagebox.showinfo("Remetente", "Numero que sera enviado as mensagens de confirmação.\n\n Numero padrão é o que esta logado no whatsapp.")
    if ajuda == "horario":
        messagebox.showinfo("Horario", "Intervalo que o programa ira rodar:\n\n\n Primeiro horario inicia a execução\n\n Ultimo horario encerra a execução.")
    if ajuda == "intervalo":
        messagebox.showinfo("Intervalo", "Intervalo que o programa buscará\npor mensagens agendadas")

def gerar_horas():
    horas = []
    for h in range(24):
        for m in (0, 30):
            horas.append(f"{h:02d}:{m:02d}")
    return horas

def criar_tela_config(raiz_principal):
    global remetente, primeira_hora, ultima_hora, intervalo
    usuario = sessao_nome()
    frame_config = tk.Frame(raiz_principal)

    # Remetente
    tk.Label(frame_config, text="Numero de confirmação:", font=("Arial", 8)).pack(pady=(20, 5),padx=5)
    frame_remetente = tk.Frame(frame_config)
    
    remetente = tk.Entry(frame_remetente , width=10)
    remetente.pack(side="left", padx=(5, 0))
    tk.Button(frame_remetente, text="?", command=lambda: mostrar_ajuda("remetente"), width=2).pack(side="left", padx=5)
    frame_remetente.pack(padx=5)

    # Horário limite de envio
    tk.Label(frame_config, text="Horario limite de envio:", font=("Arial", 8)).pack(pady=5)
    frame_horarios = tk.Frame(frame_config)
    
    horas = gerar_horas()
    
    primeira_hora = ttk.Combobox(frame_horarios, values=horas, width=7)
    primeira_hora.current(0)
    primeira_hora.pack(side='left', padx=5, pady=5)

    ultima_hora = ttk.Combobox(frame_horarios, values=horas, width=7)
    ultima_hora.current(len(horas) - 1)
    ultima_hora.pack(side='left', padx=5, pady=5)

    tk.Button(frame_horarios, text="?", command=lambda: mostrar_ajuda("horario"), width=2).pack(side='left', padx=5)
    frame_horarios.pack(pady=5)

    # Intervalo de busca
    tk.Label(frame_config, text="Intervalo de busca por agendamento:", font=("Arial", 8)).pack(pady=0)
    frame_intervalo = tk.Frame(frame_config)
    
    opcoes_intervalo = ["10min", "15min", "30min", "1h", "2h", "6h", "12h", "1dia"]
    intervalo = ttk.Combobox(frame_intervalo, values=opcoes_intervalo, width=10)
    intervalo.current(0)
    intervalo.pack(side="left", padx=(0, 5), pady=5)

    tk.Button(frame_intervalo, text="?", command=lambda: mostrar_ajuda("intervalo"), width=2).pack(side='left', padx=5)
    frame_intervalo.pack(pady=5)

    # Ajusta a janela ao conteúdo
    raiz_principal.update_idletasks()
    raiz_principal.geometry("")

    return frame_config
