from assets.interface.telas.tela_mensagem.tela_mensagem import *

def atualizar_meses(event):
    global mensagem_raiz, botao_agendar, quadro_dias, combo_31_dias, quadro_semanas, combo_semanas, combo_30_dias, combo_29_dias, combo_28_dias, combo_meses, raiz_principal
    
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

def atualizar_frequencia(event):
    global botao_agendar, quadro_meses, botao_enviar, combo_frequencia, quadro_dias, combo_31_dias, quadro_semanas, combo_semanas, combo_30_dias, combo_29_dias, combo_28_dias, quadro_meses, combo_meses, mensagem_raiz, botao_agendar, quadro_dias, combo_31_dias, quadro_semanas, combo_semanas, combo_30_dias, combo_29_dias, combo_28_dias, combo_meses, raiz_principal
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

        raiz_principal.update_idletasks()
        raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
    
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

        raiz_principal.update_idletasks()
        raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

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

        raiz_principal.update_idletasks()
        raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
