import tkinter as tk
import threading
from tkinter import Menu
from pystray import MenuItem as item, Icon
from PIL import Image, ImageDraw
from assets.interface.telas.tela_perfil.tela_perfil import criar_tela_perfil
from assets.interface.telas.tela_inicial.tela_inicial import criar_tela_inicial
from assets.interface.telas.tela_config.tela_config import criar_tela_config
from assets.interface.telas.tela_enviar.tela_enviar import tela_enviar
from assets.interface.telas.tela_mensagem.tela_mensagem import tela_mensagem
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import encerrar_chrome_existente
from assets.func.sessao.sessao import sessao_id
# Variáveis globais
raiz_principal = None
icone_bandeja = None  # Ícone da bandeja

def criar_icone():
    """Cria um ícone verde próximo ao verde do WhatsApp."""
    cor_verde_wp = (37, 211, 102)  # Verde WhatsApp
    image = Image.new("RGB", (64, 64), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 10, 54, 54), fill=cor_verde_wp)
    return image

def mostrar_tela(frame):
    """Mostra a tela desejada, verificando se a janela principal ainda existe."""
    global raiz_principal
    try:
        if raiz_principal and raiz_principal.winfo_exists():
            frame.update_idletasks()
            largura = frame.winfo_reqwidth()
            altura = frame.winfo_reqheight()
            raiz_principal.geometry(f"{largura}x{altura}")
            frame.tkraise()
        else:
            iniciar_tela_principal()
            frame.tkraise()
    except:
        iniciar_tela_principal()
        frame.tkraise()

def iniciar_tela_principal():
    """Cria ou recria a janela principal."""
    global raiz_principal
    if raiz_principal and raiz_principal.winfo_exists():
        raiz_principal.deiconify()  # Se a janela já existe, apenas a exibe novamente
        return

    raiz_principal = tk.Tk()
    raiz_principal.title("nZap - Bem vindo!")
    raiz_principal.grid_rowconfigure(0, weight=1)
    raiz_principal.grid_columnconfigure(0, weight=1)
    raiz_principal.minsize(500, 250)

    global frame0, frame1, frame3, frame4  # Manter os frames como variáveis globais
    frame0 = criar_tela_perfil(raiz_principal)
    frame1 = criar_tela_inicial(raiz_principal)
    frame3 = tela_enviar(raiz_principal)
    frame4 = tela_mensagem(raiz_principal)
    frame5 = criar_tela_config(raiz_principal)

    for frame in (frame0, frame1, frame3, frame4 , frame5
                  ):
        frame.grid(row=0, column=0, sticky="nsew")

    # Criar Menu
    menu_bar = Menu(raiz_principal)
    raiz_principal.config(menu=menu_bar)

    menu_bar.add_command(label="Perfil", command=lambda: mostrar_tela(frame0))
    menu_bar.add_command(label="Conectar", command=lambda: mostrar_tela(frame1))
    menu_bar.add_command(label="Enviar", command=lambda: mostrar_tela(frame3))
    menu_bar.add_command(label="Mensagens", command=lambda: mostrar_tela(frame4))
    menu_bar.add_command(label="Config", command=lambda: mostrar_tela(frame5))

    # Mostrar frame inicial
    mostrar_tela(frame0)

    # Modificar o comportamento do botão de fechar
    raiz_principal.protocol("WM_DELETE_WINDOW", minimizar_para_bandeja)

    raiz_principal.mainloop()

def minimizar_para_bandeja():
    """Minimiza a janela para a bandeja do sistema."""
    global raiz_principal, icone_bandeja
    if raiz_principal and raiz_principal.winfo_exists():
        raiz_principal.withdraw()  # Oculta a janela
        if not icone_bandeja:
            icone_bandeja = Icon("nZap", criar_icone(), menu=menu_bandeja)
            threading.Thread(target=icone_bandeja.run, daemon=True).start()

def restaurar_janela(icon, item):
    """Restaura a janela principal a partir do ícone da bandeja."""
    global raiz_principal
    iniciar_tela_principal()

def sair_do_programa(icon, item):
    encerrar_chrome_existente(sessao_id())
    """Fecha completamente o programa."""
    global raiz_principal, icone_bandeja
    if icone_bandeja:
        icone_bandeja.stop()
    if raiz_principal and raiz_principal.winfo_exists():
        raiz_principal.destroy()

# Criando o menu do ícone da bandeja
menu_bandeja = (
    item("Abrir Janela", restaurar_janela),
    item("Sair", sair_do_programa)
)


# Iniciar o programa
iniciar_tela_principal()