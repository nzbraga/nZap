import os
import tkinter as tk
from assets.func.sessao.sessao import sessao_id, sessao_nome
from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import start_whatsapp, whatsapp_api

id_usuario = sessao_id()

def atualizar_interface(status_label, info_label, botao_conectar, botao_desconectar):
    """ Atualiza os elementos da interface com base no estado da API """
    if whatsapp_api.api_logada:
        status_label.config(text="WhatsApp Conectado!", fg="green")
        info_label.config(text="Pronto para enviar mensagens!\nClique em desconectar para sair.")
        botao_conectar.pack_forget()
        botao_desconectar.pack(pady=5)
    else:
        status_label.config(text="WhatsApp Desconectado!", fg="red")
        info_label.config(text="Conecte ao WhatsApp\npara enviar e agendar mensagens.")
        botao_desconectar.pack_forget()
        botao_conectar.pack(pady=5)

def criar_tela_inicial(raiz_principal):
    usuario = sessao_nome().upper()
    frame_inicial = tk.Frame(raiz_principal)
    
    tk.Label(frame_inicial, text=f"{usuario}, bem-vindo ao nZap!", font=("Arial", 14)).pack(pady=5)

    # 🔥 Criar os widgets ANTES de chamá-los
    status_label = tk.Label(frame_inicial, font=("Arial", 14))
    status_label.pack(pady=(10, 5))

    info_label = tk.Label(frame_inicial, font=("Arial", 14))
    info_label.pack(pady=5)

    botao_conectar = tk.Button(frame_inicial, text="Conectar", font=("Arial", 14), bg='green', 
                               command=lambda: start_whatsapp(id_usuario))
    botao_desconectar = tk.Button(frame_inicial, text="Desconectar", font=("Arial", 10), bg='orange', 
                                  command=lambda: setattr(whatsapp_api, 'api_logada', not whatsapp_api.api_logada))

    # 🔥 Atualiza a interface uma vez ao iniciar
    atualizar_interface(status_label, info_label, botao_conectar, botao_desconectar)

    # 🔥 Registra a função de atualização automática
    whatsapp_api.atualizar_interface_callback = lambda: atualizar_interface(status_label, info_label, botao_conectar, botao_desconectar)

    raiz_principal.update_idletasks()  
    raiz_principal.geometry("")  


    return frame_inicial
