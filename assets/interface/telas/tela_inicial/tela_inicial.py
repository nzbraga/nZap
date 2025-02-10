import os
import tkinter as tk


import assets.func.login.checar_logado.checar_logado as checar_logado

def manusear_deslogar(raiz):
    raiz.destroy()

    caminho_arquivo = 'assets/arquivos/sessao/.sessao.json'
    
    if os.path.exists(caminho_arquivo):  # Verifica se o arquivo existe
        os.remove(caminho_arquivo)  # Remove o arquivo
        print("Arquivo apagado com sucesso.")
    else:
        print("Arquivo não encontrado.")
    
    from assets.interface.telas.tela_login.tela_login import tela_login
    tela_login()



def criar_tela_inicial(raiz_principal):
   


    raiz_principal.update_idletasks()
    raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
    
    #conectado ao whatsapp
    logado = True

    frame_inicial = tk.Frame(raiz_principal, bg="white")
    tk.Label(frame_inicial, text="Bem Vindo ao nZap! ", font=("Arial", 14)).pack(padx=5, pady=(50,5))

    if logado:
        tk.Label(frame_inicial, text="Conectado!", font=("Arial", 14)).pack(padx=5, pady=(20,5))
        tk.Label(frame_inicial, text="Pronto parar enviar mensagens!", font=("Arial", 12)).pack(padx=5, pady=5)
        tk.Button(frame_inicial,
                  text="Desconectar",
                  font=("Arial", 14)
                  #deslogar a sessao do whatsapp
                  ).pack(expand=True)
        tk.Button(frame_inicial,
                  text="Deslogar",
                  font=("Arial", 14),
                  command=lambda: manusear_deslogar(raiz_principal)
                  ).pack(expand=True)
        
    else:
        tk.Label(frame_inicial, text="Conecte ao WhatsApp para\nenviar mensagens\nou agendar mensagens futuras ", font=("Arial", 12)).pack(expand=True)
        tk.Label(frame_inicial, text="Descnectado!", font=("Arial", 12)).pack(expand=True)
        tk.Button(frame_inicial, text="Conectar", font=("Arial", 14)).pack(expand=True)

    return frame_inicial
