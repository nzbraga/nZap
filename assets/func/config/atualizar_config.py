import json
from pathlib import Path

from assets.func.sessao.sessao import sessao_id
from assets.func.agendamento.checar_agendamento.checar_agendamento import iniciar_checar_agendamentos, ARQUIVO_AGENDADO

usuario_id = sessao_id()

base_dir = Path.home() / "nZap"
config_dir = base_dir / "config"



# usar o ** pra atualizar apenas os valores fornecidos no fotmato 'chave': 'valor'
def atualizar_config(id, **novos_dados):
    try:
        file_path = config_dir / f"{id}.json"

        if not file_path.exists():
            print(f"Arquivo '{file_path}' não encontrado para atualização.")
            return False

        # Carrega a configuração existente
        with open(file_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        #print(f"Configuração carregada: {config}")
        # Atualiza os valores com os novos dados
        config.update(novos_dados)

        # Salva novamente
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=4)

        #print(f"Configuração atualizada com sucesso: {config}")
        iniciar_checar_agendamentos()
        return True

    except Exception as e:
        print(f"Erro ao atualizar configuração: {e}")
        return False
