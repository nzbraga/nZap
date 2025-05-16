import json
import time
import threading
from datetime import datetime
from pathlib import Path
import tkinter as tk

from assets.func.sessao.sessao import sessao_id, sessao_nome
from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import start_whatsapp, whatsapp_api
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import desconectar_whatsapp
from assets.interface.uteis.atualizar_interface import atualizar_interface
from assets.func.uteis.popUp import popUp

def criar_tela_inicial(raiz_principal):
    usuario = sessao_nome()
    frame_inicial = tk.Frame(raiz_principal)
    
    tk.Label(frame_inicial, text=f"{usuario}, bem-vindo ao nZap!", font=("Arial", 14)).pack(pady=5)

    frame_botoes = tk.Frame(frame_inicial)
    frame_botoes.pack(pady=5)

    botao_visivel = tk.Button(frame_botoes, text="Visível", font=("Arial", 10), bg='green', command=lambda: start_whatsapp(sessao_id(), False))
    botao_invisivel = tk.Button(frame_botoes, text="Invisível", font=("Arial", 10), bg='gray', command=lambda: start_whatsapp(sessao_id()))

    botao_visivel.pack(side='left', padx=5)
    botao_invisivel.pack(side='left', padx=5)

    status_label = tk.Label(frame_inicial, font=("Arial", 14))
    status_label.pack(pady=(10, 5))

    info_label = tk.Label(frame_inicial, font=("Arial", 14))
    info_label.pack(pady=5)

    botao_conectar = tk.Button(frame_inicial, text="Conectar", font=("Arial", 14), bg='green', 
                               command=lambda: start_whatsapp(sessao_id()))
    botao_desconectar = tk.Button(frame_inicial, text="Desconectar", font=("Arial", 10), bg='orange', 
                                  command=lambda: [(setattr(whatsapp_api, 'api_logada', not whatsapp_api.api_logada)),desconectar_whatsapp()])

    # 🔥 Atualiza a interface uma vez ao iniciar
    atualizar_interface(status_label, info_label, botao_conectar, botao_desconectar)

    # 🔥 Registra a função de atualização automática
    whatsapp_api.atualizar_interface_callback = lambda: atualizar_interface(status_label, info_label, botao_conectar, botao_desconectar)

    raiz_principal.update_idletasks()  
    raiz_principal.geometry("")  


    return frame_inicial
