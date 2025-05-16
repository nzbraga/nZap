import tkinter as tk
from PIL import Image, ImageTk

def config_page_tk(titulo, lar, alt, raiz):
    """
    logo = Image.open("logo_nzap.ico")    
    logo = logo.resize((30, 30))  
    logo_tk = ImageTk.PhotoImage(logo)   
    raiz.iconphoto(True, logo_tk)
    """
    raiz = tk.Tk()
    raiz.title(titulo)
    raiz.geometry(f"{lar}x{alt}")
    largura_janela = int(lar) 
    altura_janela = int(alt)
    largura_tela = raiz.winfo_screenwidth()
    altura_tela = raiz.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    raiz.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    return raiz