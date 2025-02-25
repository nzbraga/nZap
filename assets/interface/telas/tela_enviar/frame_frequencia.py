import os
import tkinter as tk
from tkinter import ttk

from assets.interface.telas.tela_enviar.uteis.opcoes_frequencia import *
from assets.interface.telas.tela_enviar.uteis.ano_bissexto import ano_bissexto

from assets.func.mensagem.montar_msg.agendar_msg import agendar_msg

lista_paginas = []
frequencia_envio = None

def tela_frequencia(origem, mensagem):
    global combo_frequencia, combo_meses, combo_semanas, combo_31_dias, combo_30_dias, combo_29_dias, combo_28_dias,lista_paginas
        
    raiz_frequancia = tk.Tk()
    raiz_frequancia.title("Frequência de Envio")
    raiz_frequancia.geometry("400x400")
    
    frame_frequencia = tk.Frame(raiz_frequancia)  # Criando o frame principal
    frame_frequencia.pack(pady=20)


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

            

        
        

        elif selecao in ["Aniversario", "Vencimento", "Diario"]:
            frequencia_envio = selecao
            botao_agendar.pack(pady=10) 
    

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

            
        elif selecao ==  "Unica":
            frequencia_envio = selecao
            botao_agendar.pack_forget()

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
    command=lambda: agendar_msg(origem, mensagem, frequencia_envio)
        
    )
    botao_agendar.pack_forget()

    return frame_frequencia