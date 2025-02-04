import tkinter as tk


from assets.func.login.uteis.alternar_senha import alternar_senha
from assets.interface.uteis.config_tela import config_page_tk
from assets.func.login.criar_usuario.criar_usuario import criar_usuario
from assets.interface.uteis.campo_obrigatorio import campo_obrigatorio, campo
from assets.func.uteis.popUp import popUp

def manusear_voltar(raiz):
    from assets.interface.telas.tela_login.tela_login import tela_login
    raiz.destroy()
    tela_login()


def tela_criar_usuario():
    
    criar_usuario_raiz = config_page_tk(
        "Login", "300", "600", 'criar_usuario_raiz')
    

    usuario = campo_obrigatorio(criar_usuario_raiz, "campo_usuario", "Usuario:", criar_usuario_raiz)

    email = campo_obrigatorio(criar_usuario_raiz, "campo_email", "Email:", criar_usuario_raiz)
    confirmar_email = campo_obrigatorio(criar_usuario_raiz, "campo_email", "Confirmar email:", criar_usuario_raiz)

    telefone = campo(criar_usuario_raiz, "campo_telefone", "Telefone:", criar_usuario_raiz)
    confirmar_telefone = campo(criar_usuario_raiz, "campo_telefone", "Confirmar telefone:", criar_usuario_raiz)
 
    senha = campo_obrigatorio(criar_usuario_raiz, "campo_senha", "Senha:", criar_usuario_raiz, True)
    confirmar_senha =campo_obrigatorio(criar_usuario_raiz, "campo_senha", "Confirmar Senha:", criar_usuario_raiz, True)

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
    
    quadro_botoes = tk.Frame(criar_usuario_raiz)
    quadro_botoes.pack(pady=10)

    btn_cancelar = tk.Button(
        quadro_botoes,
        text="Salvar",
        command=lambda:
        criar_usuario(
            usuario,
            senha, confirmar_senha,
            email, confirmar_email,
            telefone, confirmar_telefone

        ))
    btn_cancelar.pack(side="left", padx=10) 

    btn_voltar = tk.Button(
        quadro_botoes, text="Voltar",
        command=lambda:
        manusear_voltar(
            criar_usuario_raiz
        ))
    btn_voltar.pack(padx=10)



    criar_usuario_raiz.mainloop()