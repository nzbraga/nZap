import os
import tkinter as tk
from tkinter import ttk

from assets.interface.telas.tela_mensagem.uteis.opcoes_frequencia import *
from assets.interface.telas.tela_mensagem.uteis.ano_bissexto import ano_bissexto
from assets.func.mensagem.montar_msg.montar_msg import montar_msg
from assets.func.mensagem.definir_origem.definir_origem import definir_origem
from assets.func.planilha.info_planilha.info_planilha import listar_paginas

from assets.func.uteis.popUp import popUp

lista_paginas = []
def tela_mensagem(raiz_principal):
    global combo_frequencia, combo_meses, combo_semanas, combo_31_dias, combo_30_dias, combo_29_dias, combo_28_dias, botao_agendar,  botao_enviar, lista_paginas
    
    mensagem_raiz = tk.Frame(raiz_principal) 
    frame_checkbuttons = tk.Frame(mensagem_raiz)
    frame_checkbuttons.pack(pady=(15,5))
    
    frame_escolher_pagina = tk.Frame(mensagem_raiz)
    frame_escolher_pagina.pack(pady=5)

    def atualizar_frequencia(event):
        mensagem_raiz.update_idletasks()
        selecao = combo_frequencia.get()
        
        
        if selecao in ["Mensal"]:

            quadro_dias.pack(pady=5)
            combo_31_dias.pack(pady=5)
            quadro_ajuda.pack(pady=5)

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            quadro_meses.pack_forget()
            combo_meses.pack_forget()

            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
            botao_agendar.pack_forget()
           

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
        
        elif selecao == "Semanal" or selecao == "Quinzanal":
            quadro_semanas.pack(pady=5)
            combo_semanas.pack(pady=5)
            quadro_ajuda.pack(pady=5)
            
            quadro_meses.pack_forget()
            combo_meses.pack_forget()

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
            botao_agendar.pack_forget()

           

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao == "Anual":
            quadro_meses.pack(pady=5)
            combo_meses.pack(pady=5)  
            quadro_ajuda.pack(pady=5)

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()            
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
            botao_agendar.pack_forget()

            

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao in ["Aniversario", "Vencimento", "Diario"]:
            botao_agendar.pack(pady=10) 
            botao_enviar.pack_forget()

            quadro_meses.pack_forget()
            combo_meses.pack_forget()

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            quadro_ajuda.pack_forget()

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
            
        elif selecao ==  "Unica":
            botao_agendar.pack_forget()
            botao_enviar.pack(pady=10)

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            quadro_meses.pack_forget()
            combo_meses.pack_forget()

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            quadro_ajuda.pack_forget()

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
           
    def atualizar_meses(event):
        
        mensagem_raiz.update_idletasks()
        selecao = combo_meses.get()

        if selecao in ["Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"]:

            quadro_dias.pack(pady=5)
            combo_31_dias.pack(pady=5)
            botao_agendar.pack(pady=10)

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao == "Fevereiro":
            if ano_bissexto():
                quadro_dias.pack(pady=5)
                combo_29_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                quadro_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()                
                combo_30_dias.pack_forget()               
                combo_28_dias.pack_forget()

                raiz_principal.update_idletasks()
                raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
            else:
            
                quadro_dias.pack(pady=5)
                combo_28_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                quadro_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()
                combo_30_dias.pack_forget()
                combo_29_dias.pack_forget()
                
                raiz_principal.update_idletasks()
                raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao in ["Abril", "Junho", "Setembro", "Novembro"]:
        
            quadro_dias.pack(pady=5)
            combo_30_dias.pack(pady=5)
            botao_agendar.pack(pady=10)

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            combo_31_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            raiz_principal.update_idletasks()
            raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

    def atualizar_semanas(event):
        mensagem_raiz.update_idletasks()
        selecao = combo_semanas.get()

        if selecao:
            quadro_ajuda.pack_forget()
            botao_agendar.pack(pady=10)
        raiz_principal.update_idletasks()
        raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")   
    
    def atualizar_dias(event):
        mensagem_raiz.update_idletasks()
        selecao = combo_31_dias.get() or combo_28_dias.get() or combo_29_dias.get() or combo_30_dias.get() 

        if selecao:
            quadro_ajuda.pack_forget()
            botao_agendar.pack(pady=10)
        
        raiz_principal.update_idletasks()
        raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

    def alternar_envio():
        global lista_paginas  # Torna a lista global para ser acessada dentro da função
        lista_paginas = listar_paginas()  # Preenche a lista com as páginas da planilha

        if enviar_excel.get():  # Se a opção Excel estiver marcada
            enviar_agenda.set(False)  # Desmarca a opção de agenda
            escolher_pagina_planilha['values'] = lista_paginas  # Atualiza os valores no combobox
            escolher_pagina_planilha.pack(pady=5)  # Exibe o combobox
            mensagem_origem.pack_forget()  # Esconde a mensagem de origem
        else:  # Se a opção Excel não estiver marcada
            mensagem_origem.pack(pady=5)  # Exibe a mensagem de origem
            escolher_pagina_planilha.pack_forget()  # Esconde o combobox

    def alternar_agenda():
        if enviar_agenda.get():
            enviar_excel.set(False)
            escolher_pagina_planilha.pack_forget()
        mensagem_origem.pack(pady=5)
            
    mensagem_origem = tk.Label(frame_escolher_pagina, text="Lembre-se de escolher para quais contato da agenda deseja enviar a mensagem\nna opçao Excel, todos os contatos da lista serão enviados")
    mensagem_origem.pack(pady=5)

    escolher_pagina_planilha = ttk.Combobox(frame_escolher_pagina, values=lambda:listar_paginas(), width=30)
    escolher_pagina_planilha.pack_forget()

    # Criando as variáveis dos Checkbuttons
    enviar_excel = tk.BooleanVar()
    check_excel = tk.Checkbutton(frame_checkbuttons, text="Enviar Excel", variable=enviar_excel, command=alternar_envio)
    check_excel.pack(side=tk.LEFT)

    enviar_agenda = tk.BooleanVar()
    check_agenda = tk.Checkbutton(frame_checkbuttons, text="Enviar Agenda", variable=enviar_agenda, command=alternar_agenda)
    check_agenda.pack(side=tk.LEFT)



    # Adicionando o label 'Mensagem' abaixo dos checkbuttons
    tk.Label(mensagem_raiz, text="Mensagem").pack(pady=5)
    entrada_mensagem = tk.Text(mensagem_raiz, width=40, height=10)
    entrada_mensagem.pack(pady=5)

    frame_frequencia = tk.Frame(mensagem_raiz)
    frame_frequencia.pack(pady=5)

    quadro_frequencia = tk.Label(mensagem_raiz, text="Frequência")
    quadro_frequencia.pack(pady=5)
    combo_frequencia = ttk.Combobox(mensagem_raiz, values=opcoes_frequencia)
    combo_frequencia.bind("<<ComboboxSelected>>", atualizar_frequencia)
    combo_frequencia.pack(pady=5)

    quadro_meses = tk.Label (mensagem_raiz, text="Meses")
    quadro_meses.pack_forget()
    combo_meses = ttk.Combobox(mensagem_raiz, values=opcoes_meses)
    combo_meses.bind("<<ComboboxSelected>>", atualizar_meses)
    combo_meses.pack_forget()

    quadro_semanas = tk.Label(mensagem_raiz, text="Dias da semana")
    quadro_semanas.pack_forget()
    combo_semanas = ttk.Combobox(mensagem_raiz, values=opcoes_semanas)
    combo_semanas.bind("<<ComboboxSelected>>", atualizar_semanas)
    combo_semanas.pack_forget()
    
    quadro_dias = tk.Label(mensagem_raiz, text="Dia")
    quadro_dias.pack_forget()
    combo_31_dias = ttk.Combobox(mensagem_raiz, values=opcoes_31_dias)
    combo_31_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_31_dias.pack_forget()
    
    combo_30_dias = ttk.Combobox(mensagem_raiz, values=opcoes_30_dias)
    combo_30_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_30_dias.pack_forget()
  
    combo_29_dias = ttk.Combobox(mensagem_raiz, values=opcoes_29_dias)
    combo_29_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_29_dias.pack_forget()

    combo_28_dias = ttk.Combobox(mensagem_raiz, values=opcoes_28_dias)
    combo_28_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_28_dias.pack_forget(),

    frame_botoes = tk.Frame(mensagem_raiz)
    frame_botoes.pack(side="bottom",  pady=(10,20))

    quadro_ajuda = tk.Label(frame_botoes, text="Escolha uma frequencia para enviar a mensagem")
    quadro_ajuda.pack(pady=5)

    botao_agendar = tk.Button(
        frame_botoes,
        text="Agendar",
        command=lambda: popUp(
            f"Agendado: {entrada_mensagem.get('1.0', tk.END)}"
            # criar agendamento
            ))
    botao_agendar.pack_forget()

    botao_enviar = tk.Button(
        frame_botoes,
        text="Enviar",
        command=lambda: montar_msg( 
            definir_origem(enviar_excel.get(),escolher_pagina_planilha.get(), enviar_agenda.get()),
            #frequencia
            entrada_mensagem.get('1.0', tk.END)            
        ))
    botao_enviar.pack_forget()
    

    return mensagem_raiz