from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
def montar_msg(contatos, mensagem):

    if not mensagem or not mensagem.strip():  # Verifica se a mensagem é vazia ou contém apenas espaços
        #print("Mensagem vazia.")
        popUp("Mensagem vazia.")

    else:

        for contato in contatos:
        
            print(f"contato: {contato["telefone"]}\nmensagem: {mensagem}")
            enviar_mensagem(contato["telefone"], mensagem)


            