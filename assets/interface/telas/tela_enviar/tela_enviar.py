import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk

from assets.interface.telas.tela_enviar.uteis.opcoes_frequencia import *
from assets.func.planilha.info_planilha.info_planilha import listar_paginas, selecionar_arquivo, arquivo_selecionado
from assets.func.mensagem.listar_mensagens.listar_mensagens import listar_mensagens


from assets.interface.telas.tela_enviar.frame_frequencia import tela_frequencia
from assets.interface.telas.tela_enviar.uteis.salvar_mensagem import salvar_mensagem
from assets.func.sessao.sessao import sessao_id


usuario_id = sessao_id()
lista_paginas = []
lista_mensagens = []

def obter_mensagem(usuario_id: str, indice: str):
    global entrada_mensagem
    base_path = Path.home() / "nZap"
    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"
    
    if not caminho_json.exists():
        print("Arquivo JSON não encontrado.")
        return None
    
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
            entrada_mensagem = dados.get(indice, "Índice não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return None



def tela_enviar(raiz_principal):
    global lista_paginas, entrada_mensagem, enviar_agenda, enviar_excel, escolher_pagina_planilha
    
    mensagem_raiz = tk.Frame(raiz_principal) 
    frame_checkbuttons = tk.Frame(mensagem_raiz)
    frame_checkbuttons.pack(pady=(15,5))
    
    frame_escolher_pagina = tk.Frame(mensagem_raiz)
    frame_escolher_pagina.pack(pady=5)
    def alternar_excel():
        global lista_paginas, arquivo_selecionado  # Torna a lista global para ser acessada dentro da função
        enviar_agenda.set(False) 

        if not arquivo_selecionado:
            selecionar_arquivo()

        if enviar_excel.get():  # Se a opção Excel estiver marcada
            escolher_pagina_planilha.pack(side=tk.LEFT)
            botao_abrir_excel.pack(side=tk.LEFT)
            lista_paginas = listar_paginas()

            if lista_paginas:  # Só atualiza se a lista não for vazia
                escolher_pagina_planilha['values'] = lista_paginas
                escolher_pagina_planilha.current(0)
            else:
                print("Nenhuma planilha foi selecionada ou erro ao carregar páginas.")
               
            
    def alternar_agenda():
        global lista_paginas  # Torna a lista global para ser acessada dentro da função
        enviar_excel.set(False)

        if enviar_agenda.get():  # Se a opção agenda estiver marcada
            escolher_pagina_planilha.pack_forget()
            botao_abrir_excel.pack_forget()

            

    escolher_pagina_planilha = ttk.Combobox(frame_escolher_pagina, width=30)
    escolher_pagina_planilha.pack_forget()

    botao_abrir_excel = tk.Button(
        frame_escolher_pagina,
        text="Abrir",
        command=lambda: alternar_excel()
                       
            )
    botao_abrir_excel.pack_forget()

    botao_abrir_agenda = tk.Button(
        frame_escolher_pagina,
        text="Abrir",
        command=lambda: alternar_agenda()
                       
            )
    botao_abrir_agenda.pack_forget()
    

    # Criando as variáveis dos Checkbuttons
    enviar_excel = tk.BooleanVar()
    check_excel = tk.Checkbutton(frame_checkbuttons, text="enviar Excel", variable=enviar_excel, command=alternar_excel)
    check_excel.pack(side=tk.LEFT)

    enviar_agenda = tk.BooleanVar()
    check_agenda = tk.Checkbutton(frame_checkbuttons, text="enviar Agenda", variable=enviar_agenda, command=alternar_agenda)
    check_agenda.pack(side=tk.LEFT)

    # Adicionando o label 'Mensagem' abaixo dos checkbuttons
    tk.Label(mensagem_raiz, text="Mensagem:").pack(pady=5)
    entrada_mensagem = tk.Text(mensagem_raiz, width=40, height=10)
    entrada_mensagem.pack(pady=5)

    botao_salvar_mensagem = tk.Button(
        mensagem_raiz,
        text="Salvar Mensagem",
        command=lambda: salvar_mensagem(usuario_id, entrada_mensagem.get("1.0", tk.END))
                       
            )
    botao_salvar_mensagem.pack(padx=5)

    escolher_mensagem = ttk.Combobox(mensagem_raiz,values=listar_mensagens(usuario_id), width=30)
    escolher_mensagem.pack(pady=5)

    botao_salvar_mensagem = tk.Button(
        mensagem_raiz,
        text="Escolher Mensagem",
        command=lambda: obter_mensagem(usuario_id,escolher_mensagem.get()))                       
    botao_salvar_mensagem.pack(padx=5)
    


    frame_frequencia = tela_frequencia(mensagem_raiz)
    frame_frequencia.pack(pady=5)  # Adiciona o frame ao layout

    return mensagem_raiz