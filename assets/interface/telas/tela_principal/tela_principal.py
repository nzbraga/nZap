import tkinter as tk
from tkinter import Menu
from assets.interface.telas.tela_principal.tela1 import criar_tela1
from assets.interface.telas.tela_principal.tela2 import criar_tela2
from assets.interface.telas.tela_principal.tela3 import criar_tela3 
def mostrar_tela(frame):
    frame.tkraise()

# Criar janela principal
root = tk.Tk()
root.title("Janela com Menu de Abas")
root.geometry("400x300")

# Criar frames para cada "tela"
frame1 = criar_tela1(root)
frame2 = criar_tela2(root)
frame3 = criar_tela3(root)

for frame in (frame1, frame2, frame3):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

# Criar Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_bar.add_command(label="Menu 1", command=lambda: mostrar_tela(frame1))
menu_bar.add_command(label="Menu 2", command=lambda: mostrar_tela(frame2))
menu_bar.add_command(label="Menu 3", command=lambda: mostrar_tela(frame3))

# Mostrar frame inicial
mostrar_tela(frame1)

root.mainloop()
