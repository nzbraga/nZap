import tkinter as tk

from assets.func.login.logar import logar
from assets.interface.telas.tela_criar_usuario.tela_criar_usuario import tela_criar_usuario
from assets.func.login.uteis.alternar_senha import alternar_senha
from assets.interface.uteis.config_tela import config_page_tk
from assets.func.login.checar_logado.checar_logado import checar_logado

from assets.func.uteis.popUp import popUp



def manusear_criar_usuario(raiz):   
    raiz.destroy()
    tela_criar_usuario()

def manusear_login(raiz, usuario, senha):
       
        logado = logar(usuario, senha)

        if not logado:
            
            return

        else:
            raiz.destroy()
            from assets.interface.telas.tela_principal.tela_principal import mostrar_tela
            mostrar_tela()
        
def checar_login(raiz):
    usuario_id = checar_logado()
    if usuario_id:
        raiz.destroy()
        from assets.interface.telas.tela_principal.tela_principal import mostrar_tela
        mostrar_tela()

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

    quadro_botoes = tk.Frame(login_raiz)
    quadro_botoes.pack(pady=10)

    btn_criar = tk.Button(
        quadro_botoes,
        text="Criar",
        font=("Arial Black",10),
        fg='blue',
        command=lambda: manusear_criar_usuario(login_raiz)
    )
    btn_criar.pack(side="left", padx=10)

    btn_logar = tk.Button(
        quadro_botoes,
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