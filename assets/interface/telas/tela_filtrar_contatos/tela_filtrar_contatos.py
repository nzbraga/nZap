import tkinter as tk
from tkinter import ttk

def tela_filtro(tree, atualizar_lista, desmarcar  ):
    desmarcar()
    def aplicar_filtro(*args):
        filtro = filtro_var.get().lower()  # Captura o texto no campo de entrada e converte para minúsculas
        for item in tree.get_children():
            valores = tree.item(item, "values")
            nome = valores[1].lower()  # Compara o nome com o filtro
            telefone = valores[2].lower()  # Compara o telefone com o filtro
            email = valores[3].lower()  # Compara o email com o filtro
            if filtro in nome or filtro in telefone or filtro in email:
                tree.item(item, tags="show")
            else:
                tree.item(item, tags="hide")

        # Atualiza as visibilidades dos itens
        for item in tree.get_children():
            if "show" in tree.item(item, "tags"):
                tree.reattach(item, '', 0)
            else:
                tree.detach(item)
            

    def limpar_filtro():
        filtro_var.set("")  # Limpa o campo de filtro
        for item in tree.get_children():
            tree.item(item, tags="show")
            tree.reattach(item, '', 0)  # Mostra todos os contatos novamente
        
        atualizar_lista()
    
    # Cria a janela de filtro
    filtro_janela = tk.Toplevel()
    filtro_janela.title("Filtrar Contatos")
    filtro_janela.geometry("400x100")
    
    filtro_var = tk.StringVar()
    
    tk.Label(filtro_janela, text="Filtrar por nome, telefone ou email:").pack(pady=5)
    filtro_entrada = tk.Entry(filtro_janela, textvariable=filtro_var, font=("Arial", 12))
    filtro_entrada.pack(pady=5)

    filtro_entrada.focus()
    
    filtro_var.trace_add("write", aplicar_filtro)  # Atualiza o filtro a cada letra digitada
    
    # Botão de limpar filtro
    tk.Button(filtro_janela, text="Limpar", command=limpar_filtro).pack(side=tk.LEFT, expand=True, padx=5, pady=5)
    
    filtro_janela.mainloop()
