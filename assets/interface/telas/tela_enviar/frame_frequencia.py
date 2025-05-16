import os
import tkinter as tk
from tkinter import ttk

from assets.interface.telas.tela_enviar.uteis.opcoes_frequencia import *
from assets.interface.telas.tela_enviar.uteis.ano_bissexto import ano_bissexto

from assets.func.mensagem.definir_origem.definir_origem import definir_origem
from assets.func.mensagem.montar_msg.enviar_msg import enviar_msg
from assets.func.mensagem.montar_msg.agendar_msg import agendar_msg
from assets.func.uteis.popUp import popUp



lista_paginas = []
frequencia_envio = None

def tela_frequencia(raiz_principal, excel, pagina, agenda,  mensagem, destinataio):
    
    global combo_frequencia, combo_meses, combo_semanas, combo_31_dias, combo_30_dias, combo_29_dias, combo_28_dias,lista_paginas
        
    
    frame_frequencia = tk.Frame(raiz_principal)  # Criando o frame principal
    frame_frequencia.pack(pady=20)

    janela_principal = raiz_principal.winfo_toplevel()
    janela_principal.geometry(f"{janela_principal.winfo_reqwidth()}x{janela_principal.winfo_reqheight()}")

    def atualizar_frequencia(event):
        global frequencia_envio
        frame_frequencia.update_idletasks()
        selecao = combo_frequencia.get()
        
        
        if selecao in ["Mensal"]:
            frequencia_envio = selecao

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
    
            botao_agendar.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
        
          
        elif selecao in ["Semanal", "Quinzanal"]:
            frequencia_envio = selecao
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
    
            botao_agendar.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
        

        elif selecao == "Anual":
            frequencia_envio = selecao
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
    
            botao_agendar.pack_forget()

            janela_principal.update_idletasks()
            janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
        

        elif selecao in ["Aniversario", "Vencimento", "Diario"]:
            frequencia_envio = selecao
            botao_agendar.pack(side=tk.LEFT, pady=10) 
            botao_enviar.pack(pady=10)

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
        
        ## usar calendario pra escolher data msg unica   
        elif selecao ==  "Unica":
            frequencia_envio = selecao
            botao_agendar.pack(pady=10)
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

            
            
            else:
            
                frame_dias.pack(pady=5)
                combo_28_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                frame_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()
                combo_30_dias.pack_forget()
                combo_29_dias.pack_forget()
                
            
            

        elif selecao in ["Abril", "Junho", "Setembro", "Novembro"]:
        
            frame_dias.pack(pady=5)
            combo_30_dias.pack(pady=5)
            botao_agendar.pack(pady=10)

            frame_semanas.pack_forget()
            combo_semanas.pack_forget()

            combo_31_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

    def atualizar_semanas(event):
        frame_frequencia.update_idletasks()
        selecao = combo_semanas.get()

        if selecao:
            frame_ajuda.pack_forget()
            botao_agendar.pack(pady=10)
      
    def atualizar_dias(event):
        frame_frequencia.update_idletasks()
        selecao = combo_31_dias.get() or combo_28_dias.get() or combo_29_dias.get() or combo_30_dias.get() 

        if selecao:
            frame_ajuda.pack_forget()
            botao_agendar.pack(pady=10)
        
  
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
    frame_frequencia,
    text="Agendar",
    command=lambda: agendar_msg(
        definir_origem(excel.get(),
                       pagina.current(),        
                       agenda.get()),
        mensagem.get('1.0', tk.END).strip(),
        frequencia_envio.lower(),
        destinataio.get('1.0', tk.END).strip()
        ),
        
    )
    botao_agendar.pack_forget()

    

    botao_enviar = tk.Button(
    frame_frequencia,
    text="Enviar",
    command=lambda: enviar_msg(
        definir_origem(excel.get(),
                       pagina.current(),        
                       agenda.get()),
        mensagem.get('1.0', tk.END).strip(),
        frequencia_envio.lower(),
        destinataio.get('1.0', tk.END).strip()
        ),
                    #print(f"origem: {definir_origem(excel.get(), agenda.get(), pagina.current())}\nfrequencia_envio: {frequencia_envio}")]
        
    )
    botao_enviar.pack_forget()

    return frame_frequencia