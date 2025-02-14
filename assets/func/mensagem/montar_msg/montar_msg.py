from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
def montar_msg(origem, mensagem):
    # recebe origem do contato, excel ou agenda
    # monta mensegem e envia
    if origem == "agenda":

        