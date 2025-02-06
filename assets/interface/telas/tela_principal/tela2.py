import tkinter as tk

def criar_tela2(root):
    frame = tk.Frame(root, bg="white")
    tk.Label(frame, text="Tela Menu 2", font=("Arial", 14)).pack(expand=True)
    return frame
