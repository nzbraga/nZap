import os
import tkinter as tk
import threading
from pathlib import Path


from assets.func.sessao.sessao import sessao_id, sessao_nome
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import encerrar_chrome_existente
from assets.func.agendamento.checar_agendamento.checar_agendamento import iniciar_checar_agendamentos

usuario_id = sessao_id()

base_dir = Path.home() / "nZap"
agendado_dir = base_dir / "agendados"
ARQUIVO_AGENDADO = agendado_dir / f".{usuario_id}.json"





def manusear_deslogar(raiz):
    encerrar_chrome_existente(usuario_id)

    base_dir = Path.home() / "nZap"
    sessao_dir = base_dir / "sessao" / ".sessao.json"
    
    if os.path.exists(sessao_dir):
        os.remove(sessao_dir)
        print("Arquivo apagado com sucesso.")
    else:
        print("Arquivo não encontrado.")
    
    from assets.interface.telas.tela_login.tela_login import tela_login
    tela_login()
    raiz.destroy()

def criar_tela_perfil(raiz_principal):
    usuario = sessao_nome() 
    if not usuario:
        from assets.interface.telas.tela_login.tela_login import tela_login
        tela_login()    
    else:
        frame_perfil = tk.Frame(raiz_principal)
        
        tk.Label(frame_perfil, text=f"{usuario}, bem-vindo ao nZap!", font=("Arial", 14)).pack(pady=5)

        # 🔥 Criar os widgets ANTES de chamá-los
        status_label = tk.Label(frame_perfil, font=("Arial", 14))
        status_label.pack(pady=5)

        tk.Button(frame_perfil, text="Checar agendamentos", font=("Arial", 12), bg='green',
                command=iniciar_checar_agendamentos).pack(pady=0)

        tk.Label(frame_perfil, text="Clique em deslogar\npara encerrar sua sessão", font=("Arial", 10)).pack(pady=0)
        tk.Button(frame_perfil, text="Deslogar", font=("Arial", 10), bg='red', 
                command=lambda: manusear_deslogar(raiz_principal)).pack(pady=0)
        
        info_label = tk.Label(frame_perfil, font=("Arial", 14))
        info_label.pack(pady=5)

        raiz_principal.update_idletasks()  
        raiz_principal.geometry("")  

        return frame_perfil
