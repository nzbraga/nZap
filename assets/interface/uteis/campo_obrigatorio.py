import tkinter as tk

def campo_obrigatorio(raiz, quadro, texto, ):
    quadro = tk.Frame(raiz)
    quadro.pack(pady=(10,5))

    tk.Label(quadro, text=texto).pack(side=tk.LEFT)
    tk.Label(quadro, text="*", fg="red").pack(side=tk.LEFT, padx=0)

    

def campo(raiz, quadro, texto,  campo):
    quadro = tk.Frame(raiz)
    quadro.pack(pady=(10,5))

    tk.Label(quadro, text=texto).pack(side=tk.LEFT)
    
    campo = tk.Entry(raiz)
    campo.pack(pady=5)
   
    return campo