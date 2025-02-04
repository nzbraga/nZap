def mostrar_senha(elemento, entrada):
    if elemento.get():
        entrada.config(show="")
    else:
        entrada.config(show="*")