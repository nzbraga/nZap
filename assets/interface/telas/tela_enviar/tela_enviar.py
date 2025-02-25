import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk

from assets.interface.telas.tela_enviar.uteis.opcoes_frequencia import *
from assets.func.planilha.info_planilha.info_planilha import listar_paginas, selecionar_arquivo, arquivo_selecionado
from assets.func.mensagem.listar_mensagens.listar_mensagens import listar_mensagens
from assets.func.mensagem.montar_msg.montar_msg import montar_msg
from assets.func.mensagem.definir_origem.definir_origem import definir_origem
from assets.func.mensagem.agendamento.agendamento import agendar_mensagem

from assets.interface.telas.tela_enviar.frame_frequencia import tela_frequencia

from assets.interface.telas.tela_enviar.uteis.obter_mensagem import obter_mensagem
from assets.interface.telas.tela_enviar.uteis.salvar_mensagem import salvar_mensagem

from assets.func.uteis.popUp import popUp
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()
lista_paginas = []
lista_mensagens = []

def atualizar_lista_mensagens():
    """Atualiza a lista de mensagens disponíveis no Combobox."""
    escolher_mensagem["values"] = listar_mensagens(usuario_id)

def salvar_e_atualizar_mensagem():
    """Salva a mensagem e atualiza o Combobox com as mensagens disponíveis."""
    salvar_mensagem(usuario_id, entrada_mensagem.get("1.0", tk.END).strip())
    atualizar_lista_mensagens()

def tela_enviar(raiz_principal):
    global lista_paginas, entrada_mensagem, enviar_agenda, enviar_excel, escolher_pagina_planilha, escolher_mensagem

    janela_principal = raiz_principal.winfo_toplevel()
    janela_principal.geometry(f"{janela_principal.winfo_reqwidth()}x{janela_principal.winfo_reqheight()}")
    
    enviar_raiz = tk.Frame(raiz_principal) 
    frame_checkbuttons = tk.Frame(enviar_raiz)
    frame_checkbuttons.pack(pady=(15,5))
    
    frame_escolher_pagina = tk.Frame(enviar_raiz)
    frame_escolher_pagina.pack(pady=5)
    
    def alternar_excel():
        global lista_paginas, arquivo_selecionado  
        enviar_agenda.set(False) 

        if not arquivo_selecionado:
            selecionar_arquivo()

        if enviar_excel.get():  
            escolher_pagina_planilha.pack(pady=5)
            #botao_abrir_excel.pack(side=tk.LEFT)            
            frame_destinatario.pack(pady=5)
            lista_paginas = listar_paginas()

            if lista_paginas:  
                escolher_pagina_planilha['values'] = lista_paginas
                escolher_pagina_planilha.current(0)
            else:
                print("Nenhuma planilha foi selecionada ou erro ao carregar páginas.")
        
        janela_principal.update_idletasks()
        janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")           
        
    def alternar_agenda():
        global lista_paginas  
        enviar_excel.set(False)

        if enviar_agenda.get(): 
            popUp('EM CONSTRUÇÃO') 
            #escolher_pagina_planilha.pack_forget()
            #botao_abrir_excel.pack_forget()
 

    escolher_pagina_planilha = ttk.Combobox(frame_escolher_pagina, width=30)
    escolher_pagina_planilha.pack_forget()

    botao_abrir_excel = tk.Button(
        frame_escolher_pagina,
        text="Abrir Excel",
        command=alternar_excel
    )
    botao_abrir_excel.pack_forget()

    botao_abrir_agenda = tk.Button(
        frame_escolher_pagina,
        text="Abrir",
        command=alternar_agenda
    )
    botao_abrir_agenda.pack_forget()

    frame_destinatario = tk.Frame(frame_escolher_pagina)
    frame_destinatario.pack_forget()

    tk.Label(frame_destinatario, text="Escolher campo\ncom contato do usuario").pack(pady=5)

    entrada_destinatario = tk.Text(frame_destinatario, width=15, height=1)
    entrada_destinatario.insert('1.0' , 'contato')
    entrada_destinatario.pack(pady=5)

    
    enviar_excel = tk.BooleanVar()
    check_excel = tk.Checkbutton(frame_checkbuttons, text="enviar Excel", variable=enviar_excel, command=alternar_excel)
    check_excel.pack(side=tk.LEFT)

    enviar_agenda = tk.BooleanVar()
    check_agenda = tk.Checkbutton(frame_checkbuttons, text="enviar Agenda", variable=enviar_agenda, command=alternar_agenda)
    check_agenda.pack(side=tk.LEFT)

    tk.Label(enviar_raiz, text="Mensagem:").pack(pady=5)
    
    frame_escolher_mensagem = tk.Frame(enviar_raiz)
    frame_escolher_mensagem.pack(pady=5)

    escolher_mensagem = ttk.Combobox(frame_escolher_mensagem, values=listar_mensagens(usuario_id), width=30)
    escolher_mensagem.pack(side=tk.LEFT)

    botao_escolher_mensagem = tk.Button(
        frame_escolher_mensagem,
        text="Selecionar",
        command=lambda: obter_mensagem(
            usuario_id,
            escolher_mensagem.current(),
            entrada_mensagem
        )
    )
    botao_escolher_mensagem.pack(padx=5)

    entrada_mensagem = tk.Text(enviar_raiz, width=40, height=10)
    entrada_mensagem.pack(pady=5)

    frame_botao = tk.Frame(enviar_raiz)
    frame_botao.pack(pady=15)

    botao_agendar = tk.Button(
    frame_botao,
    text="Agendar",
    command=lambda: tela_frequencia(
            definir_origem(
                enviar_excel.get(),
                escolher_pagina_planilha.current(),
                enviar_agenda.get()
                ),
                entrada_mensagem.get('1.0', tk.END)

    )
        )
    botao_agendar.pack(side=tk.LEFT)

    botao_enviar = tk.Button(
        frame_botao,
        text="Enviar",
        command=lambda: montar_msg( 
            definir_origem(
                enviar_excel.get(),
                escolher_pagina_planilha.current(),
                enviar_agenda.get()
                ),
                entrada_mensagem.get('1.0', tk.END)            
        ))
    botao_enviar.pack(padx=15)
    
    
    return enviar_raiz
