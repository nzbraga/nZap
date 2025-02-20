import tkinter as tk
from tkinter import ttk

from assets.interface.telas.tela_mensagem.uteis.opcoes_frequencia import *
from assets.func.planilha.info_planilha.info_planilha import listar_paginas, selecionar_arquivo
from assets.interface.telas.tela_mensagem.frame_frequencia import tela_frequencia

lista_paginas = []

def tela_mensagem(raiz_principal):
    global lista_paginas, entrada_mensagem, enviar_agenda, enviar_excel, escolher_pagina_planilha
    
    mensagem_raiz = tk.Frame(raiz_principal) 
    frame_checkbuttons = tk.Frame(mensagem_raiz)
    frame_checkbuttons.pack(pady=(15,5))
    
    frame_escolher_pagina = tk.Frame(mensagem_raiz)
    frame_escolher_pagina.pack(pady=5)

    def alternar_excel():
        global lista_paginas  # Torna a lista global para ser acessada dentro da função
        lista_paginas = listar_paginas()  # Preenche a lista com as páginas da planilha

        if enviar_excel.get():  # Se a opção Excel estiver marcada
            enviar_agenda.set(False)  # Desmarca a opção de agenda
            escolher_pagina_planilha['values'] = lista_paginas  # Atualiza os valores no combobox
            escolher_pagina_planilha.current(0)
            escolher_pagina_planilha.pack(side=tk.LEFT)  # Exibe o combobox
            botao_abrir_excel.pack(padx=5)
        
        else:  # Se a opção Excel não estiver marcada
        
            escolher_pagina_planilha.pack_forget()  # Esconde o combobox
            botao_abrir_excel.pack_forget()

    def alternar_agenda():
        if enviar_agenda.get():
            enviar_excel.set(False)
            escolher_pagina_planilha.pack_forget()
            botao_abrir_excel.pack_forget()
    
    escolher_pagina_planilha = ttk.Combobox(frame_escolher_pagina, width=30)
    escolher_pagina_planilha.pack_forget()

    botao_abrir_excel = tk.Button(
        frame_escolher_pagina,
        text="+",
        command=lambda: [selecionar_arquivo(), alternar_excel()]
                       
            )
    botao_abrir_excel.pack_forget()

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

    frame_frequencia = tela_frequencia(mensagem_raiz)
    frame_frequencia.pack(pady=5)  # Adiciona o frame ao layout

    return mensagem_raiz