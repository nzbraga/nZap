import re
from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.mensagem.saudacao.saudacao import definir_saudacao

def substituir_variaveis(mensagem, contato):
    """
    Substitui palavras iniciadas com @ pelos valores correspondentes do dicionário contato.
    Lança um erro e para a execução se uma chave não for encontrada.
    """
    def substituir(match):
        chave = match.group(1)
        if chave not in contato:
            popUp(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
            raise ValueError(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
        return contato[chave]
    
    try:
        return re.sub(r"@(\w+)", substituir, mensagem)
    except ValueError as e:
        print(e)
        return None  # Retorna None para indicar erro

def montar_msg(contatos, mensagem):
    if not contatos:
        popUp("Nenhum contato selecionado.")
        return

    if not mensagem or not mensagem.strip():
        popUp("Mensagem vazia.")
        return

    for contato in contatos:
        mensagem_personalizada = substituir_variaveis(mensagem, contato)
        if mensagem_personalizada is None:
            popUp(f"Erro ao processar mensagem para {contato.get('nome', 'Desconhecido')}.")
            return  # Interrompe a execução se houver erro

        mensagem_completa = f"{mensagem_personalizada}"
        print(f"contato: {contato['telefone']}\nmensagem: {mensagem_completa}")
        # enviar_mensagem(contato["telefone"], mensagem_completa)
