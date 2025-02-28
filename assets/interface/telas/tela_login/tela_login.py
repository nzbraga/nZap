import tkinter as tk
import time

from assets.func.login.logar import logar
from assets.interface.telas.tela_criar_usuario.tela_criar_usuario import tela_criar_usuario
from assets.func.login.uteis.alternar_senha import alternar_senha
from assets.interface.uteis.config_tela import config_page_tk
from assets.func.sessao.sessao import sessao_id
from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import start_whatsapp

from assets.func.uteis.popUp import popUp



def manusear_criar_usuario(raiz):   
    raiz.withdraw()
    tela_criar_usuario()

def manusear_login(raiz, usuario, senha):       
        logado = logar(usuario, senha)
        if not logado:            
            return
        else:
            checar_login(raiz)
        
def checar_login(raiz): 
    if sessao_id():   
        start_whatsapp(sessao_id())       
        raiz.destroy()
        from assets.interface.telas.tela_principal.tela_principal import mostrar_tela, frame0
        mostrar_tela(frame0)

def tela_login():
    
    login_raiz = config_page_tk(
        "Login", "300", "280", 'login_raiz')
    
    checar_login(login_raiz) 

    tk.Label(login_raiz, text="Usuario:").pack(pady=(20,5))
    usuario_entrada = tk.Entry(login_raiz)
    usuario_entrada.pack(pady=5)

    tk.Label(login_raiz, text="Senha:").pack(pady=5)
    senha_entrada = tk.Entry(login_raiz, show="*")
    senha_entrada.pack(pady=5)

    mostrar_senha_var = tk.BooleanVar()
    mostrar_senha_cb = tk.Checkbutton(
        login_raiz, text="Mostrar senha",
        variable=mostrar_senha_var,
        command=lambda: alternar_senha(
            mostrar_senha_var, senha_entrada
            ))
    mostrar_senha_cb.pack()

    frame_botoes = tk.Frame(login_raiz)
    frame_botoes.pack(pady=10)

    btn_criar = tk.Button(
        frame_botoes,
        text="Criar",
        font=("Arial Black",10),
        fg='blue',
        command=lambda: manusear_criar_usuario(login_raiz)
    )
    btn_criar.pack(side="left", padx=10)

    btn_logar = tk.Button(
        frame_botoes,
        text="Entrar",
        font=("Arial Black",10),
        fg='green',
        command=lambda:
        manusear_login( login_raiz, usuario_entrada.get(),
              senha_entrada.get()              
              ))
    btn_logar.pack(pady=10)

    recuperar_senha_etiqueta = tk.Button(login_raiz, text="Esqueci a senha", fg="blue",compound=tk.LEFT)
    recuperar_senha_etiqueta.config(command=lambda: popUp('Esueci a senha'))
    recuperar_senha_etiqueta.pack(pady=(5,10))

    login_raiz.mainloop()