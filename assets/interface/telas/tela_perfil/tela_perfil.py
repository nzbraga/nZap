import os
import tkinter as tk
from assets.func.sessao.sessao import sessao_id, sessao_nome

id_usuario = sessao_id()

def manusear_deslogar(raiz):
    raiz.destroy()
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Garante que estamos no diretório correto
    caminho_arquivo = os.path.join(script_dir, 'assets', 'arquivos', 'sessao', '.sessao.json')
    
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("Arquivo apagado com sucesso.")
    else:
        print("Arquivo não encontrado.")
    
    from assets.interface.telas.tela_login.tela_login import tela_login
    tela_login()

def criar_tela_perfil(raiz_principal):
    usuario = sessao_nome()
    frame_perfil = tk.Frame(raiz_principal)
    
    tk.Label(frame_perfil, text=f"{usuario}, bem-vindo ao nZap!", font=("Arial", 14)).pack(pady=5)

    # 🔥 Criar os widgets ANTES de chamá-los
    status_label = tk.Label(frame_perfil, font=("Arial", 14))
    status_label.pack(pady=(10, 5))

    tk.Label(frame_perfil, text="Clique em deslogar\npara encerrar sua sessão", font=("Arial", 10)).pack(pady=0)
    tk.Button(frame_perfil, text="Deslogar", font=("Arial", 10), bg='red', 
              command=lambda: manusear_deslogar(raiz_principal)).pack(pady=(10,5))
    
    info_label = tk.Label(frame_perfil, font=("Arial", 14))
    info_label.pack(pady=5)

    raiz_principal.update_idletasks()  
    raiz_principal.geometry("")  

    return frame_perfil
