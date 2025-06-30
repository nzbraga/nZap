import tkinter as tk
import re
import time
from tkinter import ttk, messagebox

from assets.func.sessao.sessao import sessao_id
from assets.func.config.atualizar_config import atualizar_config
from assets.func.config.abrir_config import abrir_config
from assets.func.agendamento.checar_agendamento.checar_agendamento import iniciar_checar_agendamentos, ARQUIVO_AGENDADO

numero_remetente = None
primeira_hora = None
ultima_hora = None
intervalo_envio = None
usuario_id = sessao_id()

remetente_atual = abrir_config(usuario_id).get("remetente")
primeira_hora_atual = abrir_config(usuario_id).get("primeira_hora")
ultima_hora_atual = abrir_config(usuario_id).get("ultima_hora")
intervalo_envio_atual = abrir_config(usuario_id).get("intervalo_envio")

#print(remetente_atual, primeira_hora_atual, ultima_hora_atual, intervalo_envio_atual)

def mostrar_ajuda(ajuda):
    if ajuda == "remetente":
        messagebox.showinfo("Remetente", "Numero que sera enviado as mensagens de confirmação.\n\n Numero padrão é o que esta logado no whatsapp.")
    if ajuda == "horario":
        messagebox.showinfo("Horario", "Intervalo que o programa ira rodar:\n\n\n Primeiro horario inicia a execução\n\n Ultimo horario encerra a execução.")
    if ajuda == "intervalo_envio":
        messagebox.showinfo("Intervalo", "Intervalo que o programa buscará\npor mensagens agendadas")


def manipular_atualizar_config(usuario_id,numero_remetente, primeira_hora, ultima_hora,intervalo_envio):
    
    novo_remetente = re.sub(r'\D', '', numero_remetente) 
    novo_primeira_hora = int(primeira_hora.replace("h", "").lstrip("0"))
    novo_ultima_hora = int(ultima_hora.replace("h", "").lstrip("0"))
    novo_intervalo_envio = int(intervalo_envio.replace("h", "").lstrip("0"))
    
    atualizar_config(usuario_id, remetente=novo_remetente, primeira_hora=novo_primeira_hora, ultima_hora=novo_ultima_hora, intervalo_envio=novo_intervalo_envio)
    time.sleep(1)
    iniciar_checar_agendamentos()

def gerar_horas():
    horas = []
    for h in range(24):
            horas.append(f"{h:02d}")
    
    return horas

def criar_tela_config(raiz_principal):
    global remetente, primeira_hora, ultima_hora, intervalo_envio
    #usuario = sessao_nome()
    frame_config = tk.Frame(raiz_principal)

# Remetente
    tk.Label(frame_config, text="Numero de confirmação:", font=("Arial", 8)).pack(pady=(20, 5), padx=5)
    frame_remetente = tk.Frame(frame_config)

    entrada_remetente = tk.Entry(frame_remetente, width=10)
    if remetente_atual is not None:
        entrada_remetente.insert(0, remetente_atual)  

    entrada_remetente.pack(side="left", padx=(5, 0))

    tk.Button(frame_remetente, text="?", command=lambda: mostrar_ajuda("remetente"), width=2).pack(side="left", padx=5)
    frame_remetente.pack(padx=5)

    # Horário limite de envio
    tk.Label(frame_config, text="Horario limite de envio:", font=("Arial", 8)).pack(pady=5)
    frame_horarios = tk.Frame(frame_config)
    
    horas = gerar_horas()
    
    primeira_hora = ttk.Combobox(frame_horarios, values=horas, width=7)
    primeira_hora.insert(0, f'{primeira_hora_atual:02d}h')
    primeira_hora.pack(side='left', padx=5, pady=5)

    ultima_hora = ttk.Combobox(frame_horarios, values=horas, width=7)
    ultima_hora.insert(0, f'{ultima_hora_atual:02d}h')
    ultima_hora.pack(side='left', padx=5, pady=5)

    tk.Button(frame_horarios, text="?", command=lambda: mostrar_ajuda("horario"), width=2).pack(side='left', padx=5)
    frame_horarios.pack(pady=5)

    # Intervalo de busca
    tk.Label(frame_config, text="Intervalo de busca por agendamento:", font=("Arial", 8)).pack(pady=0)
    frame_intervalo = tk.Frame(frame_config)
    
    opcoes_intervalo = ["1", "2", "6", "12", "24"]
    intervalo_envio = ttk.Combobox(frame_intervalo, values=opcoes_intervalo, width=10)
    intervalo_envio.insert(0, f'{intervalo_envio_atual:02d}h')
    intervalo_envio.pack(side="left", padx=(0, 5), pady=5)

    tk.Button(frame_intervalo, text="?", command=lambda: mostrar_ajuda("intervalo_envio"), width=2).pack(side='left', padx=5)
    frame_intervalo.pack(pady=5)

    tk.Button(frame_config, text="Salvar", command=lambda: manipular_atualizar_config(usuario_id, entrada_remetente.get(), primeira_hora.get(), ultima_hora.get(),intervalo_envio.get()), font=("Arial", 10)).pack(pady=5)

    # Ajusta a janela ao conteúdo
    raiz_principal.update_idletasks()
    raiz_principal.geometry("")

    return frame_config
