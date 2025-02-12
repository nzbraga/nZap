import os
import threading
from threading import Thread
import tkinter as tk
from assets.func.sessao.sessao import sessao_nome
from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import start_whatsapp

logado = False  # Estado de conexão

nome_usuario = sessao_nome().upper()

def manusear_deslogar(raiz):
    raiz.destroy()

    caminho_arquivo = 'assets/arquivos/sessao/.sessao.json'
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("Arquivo apagado com sucesso.")
    else:
        print("Arquivo não encontrado.")
    
    from assets.interface.telas.tela_login.tela_login import tela_login
    tela_login()

def simula_logar(status_label, botao_conectar, botao_desconectar, info_label):
    global logado
    logado = not logado  # Alterna entre conectado e desconectado
    
    if logado:
        status_label.config(text="WhatsApp Conectado!", fg="green")
        info_label.config(text="Pronto para enviar mensagens!\nClique em desconectar para sair.")
        botao_conectar.pack_forget()  # Oculta o botão de conectar
        botao_desconectar.pack(pady=5)  # Exibe o botão de desconectar
    else:
        status_label.config(text="WhatsApp Desconectado!", fg="red")
        info_label.config(text="Conecte ao WhatsApp\npara enviar e agendar mensagens futuras.")
        botao_desconectar.pack_forget()  # Oculta o botão de desconectar
        botao_conectar.pack(pady=5)  # Exibe o botão de conectar

def criar_tela_inicial(raiz_principal):
    global logado
    usuario = sessao_nome().upper()

    frame_inicial = tk.Frame(raiz_principal, bg="white")
    
    tk.Label(frame_inicial, text=f"{usuario}, bem-vindo ao nZap!", font=("Arial", 14)).pack(pady=5)

    tk.Label(frame_inicial, text="Clique em deslogar para encerrar sua sessão", font=("Arial", 10)).pack(pady=0)
    tk.Button(frame_inicial, text="Deslogar", font=("Arial", 10), bg='red', command=lambda: manusear_deslogar(raiz_principal)).pack(pady=5)

    status_label = tk.Label(frame_inicial, text="WhatsApp Conectado!" if logado else "WhatsApp Desconectado!", 
                            font=("Arial", 14), fg="green" if logado else "red")
    status_label.pack(pady=(20, 5))

    info_label = tk.Label(frame_inicial, text="Pronto para enviar mensagens!\nClique em desconectar para sair." if logado 
                          else "Conecte ao WhatsApp\npara enviar e agendar mensagens futuras.", font=("Arial", 14))
    info_label.pack(pady=5)

    botao_conectar = tk.Button(frame_inicial, text="Conectar", font=("Arial", 14), bg='green', 
                               command=lambda:
                               start_whatsapp(nome_usuario))
    botao_desconectar = tk.Button(frame_inicial, text="Desconectar", font=("Arial", 10), bg='orange', 
                                  command=lambda: simula_logar(status_label, botao_conectar, botao_desconectar, info_label))

    if logado:
        botao_desconectar.pack(pady=(5,50))
    else:
        botao_conectar.pack(pady=(5,50))

    raiz_principal.update_idletasks()  # Garante que o layout seja atualizado
    raiz_principal.geometry("") 

    return frame_inicial
