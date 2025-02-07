import os
import tkinter as tk
from tkinter import ttk

from assets.interface.uteis.config_tela import config_page_tk
from assets.interface.telas.tela_mensagem.uteis.opcoes_frequencia.opcoes_frequencia import *
from assets.interface.telas.tela_mensagem.uteis.ano_bissexto import ano_bissexto

from assets.func.uteis.popUp import popUp

def tela_mensagem(raiz_principal):
    global combo_frequencia, combo_31_dias,combo_30_dias,combo_29_dias,combo_28_dias, combo_semanas, botao_agendar, combo_meses, botao_enviar
    
    mensagem_raiz = tk.Frame(raiz_principal)
    #mensagem_raiz = config_page_tk("Mensagem", "400", "400", raiz_principal)

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

        elif selecao == "Fevereiro":
            if ano_bissexto():
            
                combo_29_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                quadro_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()                
                combo_30_dias.pack_forget()               
                combo_28_dias.pack_forget()
            else:
            
                combo_28_dias.pack(pady=5)
                botao_agendar.pack(pady=10)

                quadro_semanas.pack_forget()
                combo_semanas.pack_forget()

                combo_31_dias.pack_forget()
                combo_30_dias.pack_forget()
                combo_29_dias.pack_forget()

        elif selecao in ["Abril", "Junho", "Setembro", "Novembro"]:
        
            combo_30_dias.pack(pady=5)
            botao_agendar.pack(pady=10)

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            combo_31_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()
      
    def atualizar_frequencia(event):
        mensagem_raiz.update_idletasks()
        selecao = combo_frequencia.get()
        
        if selecao in ["Mensal"]:
            quadro_dias.pack(pady=5)
            combo_31_dias.pack(pady=5)

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            quadro_meses.pack_forget()
            combo_meses.pack_forget()

            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()
        
        elif selecao == "Semanal" or selecao == "Quinzanal":
            quadro_semanas.pack(pady=5)
            combo_semanas.pack(pady=5)

            botao_agendar.pack(pady=10)
            
            quadro_meses.pack_forget()
            combo_meses.pack_forget()

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()  

        elif selecao == "Anual":
            quadro_meses.pack(pady=5)
            combo_meses.pack(pady=5)  

            quadro_semanas.pack_forget()
            combo_semanas.pack_forget()

            quadro_dias.pack_forget()
            combo_31_dias.pack_forget()
            combo_30_dias.pack_forget()            
            combo_29_dias.pack_forget()
            combo_28_dias.pack_forget()

            botao_enviar.pack_forget()  

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
    
    tk.Label(mensagem_raiz, text="Mensagem").pack(pady=5)
    entrada_mensagem = tk.Text(mensagem_raiz, width=40, height=5)
    entrada_mensagem.pack(pady=5)
    
    opcoes_frequencia = [f"{frequencia}" for frequencia in frequencias]
    opcoes_meses = [f"{frequencia}" for frequencia in meses]
    opcoes_semanas = [f"{frequencia}" for frequencia in semanas]
    opcoes_31_dias = [f"{dia:02}" for dia in range(1, 32)]
    opcoes_30_dias = [f"{dia:02}" for dia in range(1, 31)]
    opcoes_29_dias = [f"{dia:02}" for dia in range(1, 30)]
    opcoes_28_dias = [f"{dia:02}" for dia in range(1, 29)]

    frame_frequencia = tk.Frame(mensagem_raiz)
    frame_frequencia.pack(pady=5)


    quadro_frequencia = tk.Label(mensagem_raiz, text="Frequência")
    quadro_frequencia.pack(pady=5)
    combo_frequencia = ttk.Combobox(mensagem_raiz, values=opcoes_frequencia)
    combo_frequencia.pack(pady=5)
    combo_frequencia.bind("<<ComboboxSelected>>", atualizar_frequencia)

    quadro_semanas = tk.Label(mensagem_raiz, text="Dias da semana")
    quadro_semanas.pack_forget()
    combo_semanas = ttk.Combobox(mensagem_raiz, values=opcoes_semanas)
    combo_semanas.pack_forget()
    
    quadro_meses = tk.Label (mensagem_raiz, text="Meses")
    quadro_meses.pack_forget()
    combo_meses = ttk.Combobox(mensagem_raiz, values=opcoes_meses)
    combo_meses.bind("<<ComboboxSelected>>", atualizar_meses)
    combo_meses.pack_forget()
    
    quadro_dias = tk.Label(mensagem_raiz, text="Dia")
    quadro_dias.pack_forget()
    combo_31_dias = ttk.Combobox(mensagem_raiz, values=opcoes_31_dias)
    combo_31_dias.pack_forget()
    
    combo_30_dias = ttk.Combobox(mensagem_raiz, values=opcoes_30_dias)
    combo_30_dias.pack_forget()
  
    combo_29_dias = ttk.Combobox(mensagem_raiz, values=opcoes_29_dias)
    combo_29_dias.pack_forget()

    combo_28_dias = ttk.Combobox(mensagem_raiz, values=opcoes_28_dias)
    combo_28_dias.pack_forget(),

    frame_botoes = tk.Frame(mensagem_raiz)
    frame_botoes.pack(side="bottom",  pady=(10,20))

    botao_agendar = tk.Button(
        frame_botoes,
        text="Agendar",
        command=lambda: popUp(
            f"Agendado: {entrada_mensagem.get('1.0', tk.END)}"
            ))
    botao_agendar.pack_forget()

    botao_enviar = tk.Button(
        frame_botoes,
        text="Enviar",
        command=lambda: popUp(
            f"Enviado: {entrada_mensagem.get('1.0', tk.END)}"
            ))
    botao_enviar.pack_forget()
    

    return mensagem_raiz