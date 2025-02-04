def alternar_senha(elemento, entrada, entrada2=None):
   
    if entrada2:    
        if elemento.get():
            entrada.config(show="")
            entrada2.config(show="")
        else:
            entrada.config(show="*")
            entrada2.config(show="*")
    else:  
        if elemento.get():
            entrada.config(show="")
        else:
            entrada.config(show="*")