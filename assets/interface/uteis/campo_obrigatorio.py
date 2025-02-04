import tkinter as tk

def campo_obrigatorio(raiz, quadro, texto,  campo, mostrar=False):
    quadro = tk.Frame(raiz)
    quadro.pack(pady=(10,5))

    tk.Label(quadro, text=texto).pack(side=tk.LEFT)
    tk.Label(quadro, text="*", fg="red").pack(side=tk.LEFT, padx=0)

    if mostrar:
        campo = tk.Entry(raiz, show="*")
    else:
        campo = tk.Entry(raiz)
    campo.pack(pady=5)
   
    return campo

def campo(raiz, quadro, texto,  campo):
    quadro = tk.Frame(raiz)
    quadro.pack(pady=(10,5))

    tk.Label(quadro, text=texto).pack(side=tk.LEFT)
    
    campo = tk.Entry(raiz)
    campo.pack(pady=5)
   
    return campo