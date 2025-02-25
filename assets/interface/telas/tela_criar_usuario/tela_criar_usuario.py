import tkinter as tk


from assets.func.login.uteis.alternar_senha import alternar_senha
from assets.interface.uteis.config_tela import config_page_tk
from assets.func.login.criar_usuario.criar_usuario import criar_usuario
from assets.interface.uteis.campo_obrigatorio import campo_obrigatorio, campo
from assets.func.uteis.popUp import popUp

def manusear_voltar(raiz):
    from assets.interface.telas.tela_login.tela_login import tela_login
    raiz.withdraw()
    tela_login()

def manusear_criar_usuario(
        raiz,
        usuario,
        senha, confirmar_senha,
        email, confirmar_email,
        telefone, confirmar_telefone
        ):
    criado = criar_usuario( usuario, senha, confirmar_senha, email, confirmar_email, telefone, confirmar_telefone)
    if criado:
        from assets.interface.telas.tela_login.tela_login import tela_login
        raiz.withdraw()
        tela_login()
    


def tela_criar_usuario():

    criar_usuario_raiz = config_page_tk(
        "Login", "350", "350", 'criar_usuario_raiz')    

    campo_obrigatorio(criar_usuario_raiz, "campo_usuario", "Usuario:")
    usuario = tk.Entry(criar_usuario_raiz)
    usuario.pack()

    frame_emails = tk.Frame(criar_usuario_raiz)
    frame_emails.pack(pady=(10, 5))
    
    frame_email = tk.Frame(frame_emails)
    frame_email.pack(side=tk.LEFT, padx=5)
    campo_obrigatorio(frame_email, "campo_email", "Email:")   
    email = tk.Entry(frame_email)
    email.pack()
    
    frame_confirmar_email = tk.Frame(frame_emails)
    frame_confirmar_email.pack(side=tk.LEFT, padx=5)
    campo_obrigatorio(frame_confirmar_email , "campo_confirmar_email", "Confirmar Email:")   
    confirmar_email = tk.Entry(frame_confirmar_email)
    confirmar_email.pack()
    
    frame_telefones = tk.Frame(criar_usuario_raiz)
    frame_telefones.pack(pady=(10, 5))
    
    frame_telefone = tk.Frame(frame_telefones)
    frame_telefone.pack(side=tk.LEFT, padx=5)
    campo_obrigatorio(frame_telefone , "campo_telefone", "telefone:")   
    telefone = tk.Entry(frame_telefone)
    telefone.pack()
    
    frame_confirmar_telefone = tk.Frame(frame_telefones)
    frame_confirmar_telefone.pack(side=tk.LEFT, padx=5)
    campo_obrigatorio(frame_confirmar_telefone , "campo_confirmar_telefone", "Confirmar telefone:")   
    confirmar_telefone = tk.Entry(frame_confirmar_telefone)
    confirmar_telefone.pack()

    frame_senhas = tk.Frame(criar_usuario_raiz)
    frame_senhas.pack(pady=(10, 5))

    frame_senha = tk.Frame(frame_senhas)
    frame_senha.pack(side=tk.LEFT, padx=5)
    campo_obrigatorio(frame_senha , "campo_senha", "Senha:")   
    senha = tk.Entry(frame_senha, show="*")
    senha.pack()

    frame_confirmar_senha = tk.Frame(frame_senhas)
    frame_confirmar_senha.pack(side=tk.LEFT, padx=5)
    campo_obrigatorio(frame_confirmar_senha , "campo_confirmar_senha", "Confirmar Senha:")   
    confirmar_senha = tk.Entry(frame_confirmar_senha, show="*")
    confirmar_senha.pack()

    mostrar_senha_var = tk.BooleanVar()
    mostrar_senha_cb = tk.Checkbutton(
        criar_usuario_raiz, text="Mostrar senha",
        variable=mostrar_senha_var,
        command=lambda: alternar_senha(
            mostrar_senha_var,
            senha,
            confirmar_senha
        ))
    mostrar_senha_cb.pack()
    
    frame_botoes = tk.Frame(criar_usuario_raiz)
    frame_botoes.pack(pady=10)

    btn_cancelar = tk.Button(
        frame_botoes,
        text="Salvar",
        command=lambda:
        manusear_criar_usuario(criar_usuario_raiz,
            usuario.get(),
            senha.get(), confirmar_senha.get(),
            email.get(), confirmar_email.get(),
            telefone.get(), confirmar_telefone.get()

        ))
    btn_cancelar.pack(side="left", padx=10) 

    btn_voltar = tk.Button(
        frame_botoes, text="Voltar",
        command=lambda:
        manusear_voltar(
            criar_usuario_raiz
        ))
    btn_voltar.pack(padx=10)



    criar_usuario_raiz.mainloop()
