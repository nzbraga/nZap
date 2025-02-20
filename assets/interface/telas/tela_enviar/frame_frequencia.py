import os
import tkinter as tk
from tkinter import ttk

from assets.interface.telas.tela_enviar.uteis.opcoes_frequencia import *
from assets.interface.telas.tela_enviar.uteis.ano_bissexto import ano_bissexto
from assets.func.mensagem.montar_msg.montar_msg import montar_msg
from assets.func.mensagem.definir_origem.definir_origem import definir_origem
from assets.interface.telas.tela_enviar.tela_enviar import *

from assets.func.uteis.popUp import popUp

lista_paginas = []

def tela_frequencia(raiz_principal):
    global combo_frequencia, combo_meses, combo_semanas, combo_31_dias, combo_30_dias, combo_29_dias, combo_28_dias, botao_agendar, botao_enviar, lista_paginas
    
    janela_principal = raiz_principal.winfo_toplevel()
    janela_principal.geometry(f"{janela_principal.winfo_reqwidth()}x{janela_principal.winfo_reqheight()}")
    
    frame_frequencia = tk.Frame(raiz_principal)  # Criando o frame principal

    def atualizar_frequencia(event):
        frame_frequencia.update_idletasks()
        selecao = combo_frequencia.get()
        
        
        if selecao in ["Mensal"]:

            frame_dias.pack(pady=5)
            combo_31_dias.pack(pady=5)
            frame_ajuda.pack(pady=5)

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            frame_meses.pack_forget()
            combo_meses.pack_forget()

            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
            botao_agendar.pack_forget()
           

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
        
        elif selecao == "Semanal" or selecao == "Quinzanal":
            frame_semanas.pack(pady=5)
            combo_semanas.pack(pady=5)
            frame_ajuda.pack(pady=5)
            
            frame_meses.pack_forget()
            combo_meses.pack_forget()

            frame_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
            botao_agendar.pack_forget()

           

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao == "Anual":
            frame_meses.pack(pady=5)
            combo_meses.pack(pady=5)  
            frame_ajuda.pack(pady=5)

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            frame_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()            
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
            botao_agendar.pack_forget()

            

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao in ["Aniversario", "Vencimento", "Diario"]:
            botao_agendar.pack(pady=10) 
            botao_enviar.pack_forget()

            frame_meses.pack_forget()
            combo_meses.pack_forget()

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            frame_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            frame_ajuda.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
            
        elif selecao ==  "Unica":
            botao_agendar.pack_forget()
            botao_enviar.pack(pady=10)

            frame_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            frame_meses.pack_forget()
            combo_meses.pack_forget()

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            frame_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            frame_ajuda.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
           
    def atualizar_meses(event):
        
        frame_frequencia.update_idletasks()
        selecao = combo_meses.get()

        if selecao in ["Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"]:

            frame_dias.pack(pady=5)
            combo_31_dias.pack(pady=5)
            botao_agendar.pack(pady=10)

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao == "Fevereiro":
            if ano_bissexto():
                frame_dias.pack(pady=5)
                combo_29_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                frame_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()                
                combo_30_dias.pack_forget()               
                combo_28_dias.pack_forget()

                janela_principal.update_idletasks()
                janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
            else:
            
                frame_dias.pack(pady=5)
                combo_28_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                frame_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()
                combo_30_dias.pack_forget()
                combo_29_dias.pack_forget()
                
                janela_principal.update_idletasks()
                janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

        elif selecao in ["Abril", "Junho", "Setembro", "Novembro"]:
        
            frame_dias.pack(pady=5)
            combo_30_dias.pack(pady=5)
            botao_agendar.pack(pady=10)

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            combo_31_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

    def atualizar_semanas(event):
        frame_frequencia.update_idletasks()
        selecao = combo_semanas.get()

        if selecao:
            frame_ajuda.pack_forget()
            botao_agendar.pack(pady=10)
        janela_principal.update_idletasks()
        janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")   
    
    def atualizar_dias(event):
        frame_frequencia.update_idletasks()
        selecao = combo_31_dias.get() or combo_28_dias.get() or combo_29_dias.get() or combo_30_dias.get() 

        if selecao:
            frame_ajuda.pack_forget()
            botao_agendar.pack(pady=10)
        
        janela_principal.update_idletasks()
        janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")


    label_frequencia = tk.Label(frame_frequencia, text="Frequência")
    label_frequencia.pack(pady=5)
    combo_frequencia = ttk.Combobox(frame_frequencia, values=opcoes_frequencia)
    combo_frequencia.bind("<<ComboboxSelected>>", atualizar_frequencia)
    combo_frequencia.pack(pady=5)

    frame_meses = tk.Label (frame_frequencia, text="Meses")
    frame_meses.pack_forget()
    combo_meses = ttk.Combobox(frame_frequencia, values=opcoes_meses)
    combo_meses.bind("<<ComboboxSelected>>", atualizar_meses)
    combo_meses.pack_forget()

    frame_semanas = tk.Label(frame_frequencia, text="Dias da semana")
    frame_semanas.pack_forget()
    combo_semanas = ttk.Combobox(frame_frequencia, values=opcoes_semanas)
    combo_semanas.bind("<<ComboboxSelected>>", atualizar_semanas)
    combo_semanas.pack_forget()
    
    frame_dias = tk.Label(frame_frequencia, text="Dia")
    frame_dias.pack_forget()
    combo_31_dias = ttk.Combobox(frame_frequencia, values=opcoes_31_dias)
    combo_31_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_31_dias.pack_forget()
    
    combo_30_dias = ttk.Combobox(frame_frequencia, values=opcoes_30_dias)
    combo_30_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_30_dias.pack_forget()
  
    combo_29_dias = ttk.Combobox(frame_frequencia, values=opcoes_29_dias)
    combo_29_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_29_dias.pack_forget()

    combo_28_dias = ttk.Combobox(frame_frequencia, values=opcoes_28_dias)
    combo_28_dias.bind("<<ComboboxSelected>>", atualizar_dias)
    combo_28_dias.pack_forget(),

    frame_botoes = tk.Frame(frame_frequencia)
    frame_botoes.pack(side="bottom",  pady=(10,20))

    frame_ajuda = tk.Label(frame_botoes, text="Escolha uma frequencia para enviar a mensagem")
    frame_ajuda.pack(pady=5)

    
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
        text="enviar",
        command=lambda: montar_msg( 
            definir_origem(
                enviar_excel.get(),
                escolher_pagina_planilha.current(),
                enviar_agenda.get()),
                entrada_mensagem.get('1.0', tk.END)            
        ))
    botao_enviar.pack_forget()
    
    

    return frame_frequencia