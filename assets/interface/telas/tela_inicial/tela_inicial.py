import tkinter as tk

conectado = False
def criar_tela_inicial(raiz_principal):
    global conectado
    frame_inicial = tk.Frame(raiz_principal, bg="white")
    tk.Label(frame_inicial, text="Bem Vindo ao nZap! ", font=("Arial", 14)).pack(expand=True)

    if conectado:
        tk.Label(frame_inicial, text="Conectado!", font=("Arial", 14)).pack(expand=True)
        tk.Label(frame_inicial, text="Pronto parar enviar mensagens!", font=("Arial", 14)).pack(expand=True)
        
    else:
        tk.Label(frame_inicial, text="Conecte seu WhatsApp para continuar", font=("Arial", 12)).pack(expand=True)
        tk.Label(frame_inicial, text="Desconectado!", font=("Arial", 12)).pack(expand=True)
        tk.Button(frame_inicial, text="Conectar", font=("Arial", 14)).pack(expand=True)

    return frame_inicial
