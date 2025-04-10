import json
import time
import threading
from datetime import datetime
from pathlib import Path
import tkinter as tk

from assets.func.sessao.sessao import sessao_id, sessao_nome
from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import start_whatsapp, whatsapp_api
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import desconectar_whatsapp, obter_dados_usuario
from assets.func.agendamento.checar_agendamento.checar_agendamento import checar_agendamentos, ARQUIVO_AGENDADO
from assets.func.agendamento.uteis.resetar_agendamentos import resetar_agendamentos
from assets.func.uteis.popUp import popUp


def atualizar_interface(status_label, info_label, botao_conectar, botao_desconectar):
    """ Atualiza os elementos da interface com base no estado da API """
    if whatsapp_api.api_logada:
        nome_logado = obter_dados_usuario()

        status_label.config(text=f"WhatsApp Conectado!\nConectado como:\n{nome_logado}", fg="green")
        info_label.config(text="Pronto para enviar mensagens!\nClique em desconectar para sair.")
        botao_conectar.pack_forget()
        botao_desconectar.pack(pady=5)

        # Inicia a thread de checagem de agendamentos após conectar ao WhatsApp
        thread = threading.Thread(target=checar_agendamentos, args=(ARQUIVO_AGENDADO,), daemon=True)
        thread.start()

        # Inicia a thread para rodar a função em segundo plano
        thread = threading.Thread(target=resetar_agendamentos, args=(ARQUIVO_AGENDADO,), daemon=True)
        thread.start()


    else:
        status_label.config(text="WhatsApp Desconectado!", fg="red")
        info_label.config(text="Conecte ao WhatsApp\npara enviar e agendar mensagens.")
        botao_desconectar.pack_forget()
        botao_conectar.pack(pady=5)

def criar_tela_inicial(raiz_principal):
    usuario = sessao_nome()
    frame_inicial = tk.Frame(raiz_principal)
    
    tk.Label(frame_inicial, text=f"{usuario}, bem-vindo ao nZap!", font=("Arial", 14)).pack(pady=5)

    # 🔥 Criar os widgets ANTES de chamá-los
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
