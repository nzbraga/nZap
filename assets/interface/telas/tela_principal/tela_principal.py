import tkinter as tk
from tkinter import Menu
from assets.interface.telas.tela_mensagem.tela_mensagem import tela_mensagem
from assets.interface.telas.tela_contatos.tela_contatos import tela_contatos
from assets.interface.telas.tela_inicial.tela_inicial import criar_tela_inicial



def mostrar_tela(frame):
    """
    Mostra a tela passada como par metro na janela principal.

    Atualiza o tamanho da janela principal com base no tamanho da tela
    passada como par metro, e a exibe na tela com tkraise().

    :param frame: Frame da tela a ser exibida
    :type frame: tkinter.Frame
    """

    raiz_principal.update_idletasks()
    raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
    frame.tkraise()

# Criar janela principal
raiz_principal = tk.Tk()
raiz_principal.title("nZap -  Bem vindo!")
raiz_principal.grid_rowconfigure(0, weight=1)
raiz_principal.grid_columnconfigure(0, weight=1)
raiz_principal.resizable(False, False)

raiz_principal.minsize(500, 200)

# Criar frames para cada "tela"
frame1 = criar_tela_inicial(raiz_principal)
frame2 = tela_mensagem(raiz_principal)
frame3 = tela_contatos(raiz_principal)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Criar Menu
menu_bar = Menu(raiz_principal)
raiz_principal.config(menu=menu_bar)

menu_bar.add_command(label="Conectar", command=lambda: mostrar_tela(frame1))
menu_bar.add_command(label="Mensagem", command=lambda: mostrar_tela(frame2))
menu_bar.add_command(label="Contatos", command=lambda: mostrar_tela(frame3))

# Mostrar frame inicial

mostrar_tela(frame1)

raiz_principal.mainloop()