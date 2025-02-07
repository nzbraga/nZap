import tkinter as tk


conectado = False
def criar_tela_inicial(raiz_principal):
    global conectado

    raiz_principal.update_idletasks()
    raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")

    from assets.interface.telas.tela_principal.tela_principal import logado

    logado

    frame_inicial = tk.Frame(raiz_principal, bg="white")
    tk.Label(frame_inicial, text="Bem Vindo ao nZap! ", font=("Arial", 14)).pack(padx=5, pady=(50,5))

    if logado:
        tk.Label(frame_inicial, text="Conectado!", font=("Arial", 14)).pack(padx=5, pady=(20,5))
        tk.Label(frame_inicial, text="Pronto parar enviar mensagens!", font=("Arial", 12)).pack(padx=5, pady=5)
        tk.Button(frame_inicial, text="Desconectar", font=("Arial", 14)).pack(expand=True)
        
    else:
        tk.Label(frame_inicial, text="Conecte ao WhatsApp para\nenviar mensagens\nou agendar mensagens futuras ", font=("Arial", 12)).pack(expand=True)
        tk.Label(frame_inicial, text="Descnectado!", font=("Arial", 12)).pack(expand=True)
        tk.Button(frame_inicial, text="Conectar", font=("Arial", 14)).pack(expand=True)

    return frame_inicial
