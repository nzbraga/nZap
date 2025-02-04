import os
from tkinter import *

from assets.interface.uteis.config_tela import config_page_tk

def tela_mensagem():
    mensagem_raiz = config_page_tk(
        "Mensagem", "300", "200", 'mensagem_raiz'
    )
    
   
    
    mensagem_raiz.mainloop()