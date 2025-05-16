import json
from pathlib import Path
from assets.func.sessao.sessao import sessao_id


limitador = 0

base_dir = Path.home() / "nZap"
agendado_dir = base_dir / "agendados"

usuario_id = sessao_id()

ARQUIVO_AGENDADO = agendado_dir / f".{usuario_id}.json"


def agendar_msg(contatos, mensagem, frequencia="hoje", chave_destinatario='contato'):
    # Verifica se o diretório agendado existe, se não, cria
    agendado_dir.mkdir(parents=True, exist_ok=True)

    #print(f'contatos>>>>: {contatos}')  

    # Cria uma lista para armazenar as mensagens agendadas
    mensagens_agendadas = []

    # Preenche as informações de cada contato
    for contato in contatos:
        # Substitui o marcador @nome na mensagem pelo nome do contato
       
        # Cria o dicionário de dados conforme o formato solicitado
        mensagem_dados = {
            "contato":  
                contato                
            ,
            "frequencia": frequencia,
            "mensagem": mensagem,
            "enviado": False  # Define como False por padrão, já que a mensagem ainda não foi enviada
        }

        # Adiciona a mensagem formatada à lista
        mensagens_agendadas.append(mensagem_dados)
    print('Agendado')
    # Salva as mensagens agendadas no arquivo JSON
    if ARQUIVO_AGENDADO.exists():
        # Se o arquivo já existir, carrega os dados existentes e adiciona as novas mensagens
        with open(ARQUIVO_AGENDADO, 'r', encoding='utf-8') as file:
            dados_existentes = json.load(file)
            dados_existentes.extend(mensagens_agendadas)

        with open(ARQUIVO_AGENDADO, 'w', encoding='utf-8') as file:
            json.dump(dados_existentes, file, ensure_ascii=False, indent=4)
    else:
        # Se o arquivo não existir, cria um novo com as mensagens
        with open(ARQUIVO_AGENDADO, 'w', encoding='utf-8') as file:
            json.dump(mensagens_agendadas, file, ensure_ascii=False, indent=4)

