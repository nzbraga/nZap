import tkinter as tk


from assets.func.login.logar import logar
from assets.func.login.uteis.mostrar_senha import mostrar_senha
from assets.func.interface.uteis.config_tela import config_page_tk
def tela_login():
    
    login_raiz = config_page_tk(
        "Login", "300", "200", 'login_raiz')
    
    tk.Label(login_raiz, text="Usuario:").pack(pady=5)
    usuario_entrada = tk.Entry(login_raiz)
    usuario_entrada.pack(pady=5)

    tk.Label(login_raiz, text="Senha:").pack(pady=5)
    senha_entrada = tk.Entry(login_raiz, show="*")
    senha_entrada.pack(pady=5)

    show_password_var = tk.BooleanVar()
    show_password_cb = tk.Checkbutton(
        login_raiz, text="Mostrar senha",
        variable=show_password_var,
        command=lambda: mostrar_senha(
            show_password_var, senha_entrada
            ))
    show_password_cb.pack()

    btn_logar = tk.Button(
        login_raiz, text="Entrar",
        command=lambda:
        logar(usuario_entrada.get(),
              senha_entrada.get()              
              ))
    btn_logar.pack(pady=10)

    login_raiz.mainloop()