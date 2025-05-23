import json
import threading
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox

from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

def carregar_mensagens(caminho_json):
    if caminho_json.exists():
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_mensagens_async(caminho_json, mensagens, callback=None):
    def salvar():
        with open(caminho_json, "w", encoding="utf-8") as arquivo:
            json.dump(mensagens, arquivo, indent=4, ensure_ascii=False)
        if callback:
            callback()
    threading.Thread(target=salvar).start()

def tela_mensagem(raiz_principal):
    base_path = Path.home() / "nZap"
    base_path.mkdir(parents=True, exist_ok=True)

    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"
    caminho_json.parent.mkdir(parents=True, exist_ok=True)

    mensagens = carregar_mensagens(caminho_json)

    mensagem_raiz = tk.Frame(raiz_principal)
    tk.Label(mensagem_raiz, text="Mensagens", font=("Arial", 14)).pack(pady=5)

    tree = ttk.Treeview(mensagem_raiz, columns=("#1", "#2"), show="headings")
    tree.heading("#1", text="Título")
    tree.heading("#2", text="Mensagem")

    tree.column("#1", width=80, anchor="w")  # Título (fixo, menor)
    tree.column("#2", width=400, anchor="w")  # Mensagem (fixo, maior)

    tree.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

    def atualizar_lista():
        tree.delete(*tree.get_children())
        for titulo, msg in mensagens.items():
            tree.insert("", tk.END, values=(titulo, msg))

    def nova_mensagem():
        def salvar_nova():
            titulo = entry_titulo.get().strip()
            mensagem = text_mensagem.get("1.0", tk.END).strip()

            if titulo and mensagem:
                mensagens[titulo] = mensagem
                salvar_mensagens_async(caminho_json, mensagens, callback=atualizar_lista)
                janela_nova.destroy()

        janela_nova = tk.Toplevel(raiz_principal)
        janela_nova.title("Nova Mensagem")
        janela_nova.geometry("400x400")

        # Título
        frame_titulo = tk.Frame(janela_nova, padx=10, pady=5)
        frame_titulo.pack(fill=tk.X)
        tk.Label(frame_titulo, text="Título:", font=("Arial", 12)).pack(anchor="w")
        entry_titulo = tk.Entry(frame_titulo, font=("Arial", 12), width=50)
        entry_titulo.pack()

        # Mensagem
        frame_mensagem = tk.Frame(janela_nova, padx=10, pady=5)
        frame_mensagem.pack(fill=tk.BOTH, expand=True)
        tk.Label(frame_mensagem, text="Mensagem:", font=("Arial", 12)).pack(anchor="w")
        text_mensagem = tk.Text(frame_mensagem, font=("Arial", 12), width=50, height=10)
        text_mensagem.pack()

        btn_frame = tk.Frame(janela_nova)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Salvar", command=salvar_nova).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancelar", command=janela_nova.destroy).pack(side=tk.LEFT, padx=5)

        janela_nova.transient(raiz_principal)
        janela_nova.grab_set()

    def editar_mensagem():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma mensagem para editar.")
            return

        item = selecionado[0]
        titulo_atual, mensagem_atual = tree.item(item, "values")

        def salvar_edicao():
            novo_titulo = entry_titulo.get().strip()
            nova_mensagem = text_mensagem.get("1.0", tk.END).strip()

            if novo_titulo and nova_mensagem:
                mensagens.pop(titulo_atual, None)
                mensagens[novo_titulo] = nova_mensagem
                salvar_mensagens_async(caminho_json, mensagens, callback=atualizar_lista)
                janela_edicao.destroy()

        janela_edicao = tk.Toplevel(raiz_principal)
        janela_edicao.title("Editar Mensagem")
        janela_edicao.geometry("400x400")

        # Título
        frame_titulo = tk.Frame(janela_edicao, padx=10, pady=5)
        frame_titulo.pack(fill=tk.X)
        tk.Label(frame_titulo, text="Título:", font=("Arial", 12)).pack(anchor="w")
        entry_titulo = tk.Entry(frame_titulo, font=("Arial", 12), width=50)
        entry_titulo.pack()

        # Mensagem
        frame_mensagem = tk.Frame(janela_edicao, padx=10, pady=5)
        frame_mensagem.pack(fill=tk.BOTH, expand=True)
        tk.Label(frame_mensagem, text="Mensagem:", font=("Arial", 12)).pack(anchor="w")
        text_mensagem = tk.Text(frame_mensagem, font=("Arial", 12), width=50, height=10)
        text_mensagem.pack()

        btn_frame = tk.Frame(janela_edicao)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Salvar", command=salvar_edicao).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancelar", command=janela_edicao.destroy).pack(side=tk.LEFT, padx=5)

        janela_edicao.transient(raiz_principal)
        janela_edicao.grab_set()

    def apagar_mensagem():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma mensagem para apagar.")
            return

        item = selecionado[0]
        titulo_atual = tree.item(item, "values")[0]

        if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta mensagem?"):
            mensagens.pop(titulo_atual, None)
            salvar_mensagens_async(caminho_json, mensagens, callback=atualizar_lista)

    btn_frame = tk.Frame(mensagem_raiz)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Nova Mensagem", command=nova_mensagem).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Editar Mensagem", command=editar_mensagem).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Apagar Mensagem", command=apagar_mensagem).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Atualizar Lista", command=atualizar_lista).pack(side=tk.LEFT, padx=5)

    atualizar_lista()

    return mensagem_raiz
