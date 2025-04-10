import json
import time
import threading
from pathlib import Path
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

base_dir = Path.home() / "nZap"
agendado_dir = base_dir / "agendados"

ARQUIVO_AGENDADO = agendado_dir / f".{usuario_id}.json"

def resetar_agendamentos(arquivo):
    
    
    
    def resetar():
        print('resetar_agendamentos ativado')
        time.sleep(86400)  # Aguarda 1 dia antes de começar

        while True:        
            try:
                print("\nVerificando se o arquivo existe...")

                if not arquivo.exists():
                    print("Arquivo JSON não encontrado.")
                    time.sleep(60)
                    continue

                print("Arquivo encontrado! Lendo conteúdo...")

                with open(arquivo, 'r', encoding='utf-8') as f:
                    try:
                        dados = json.load(f)
                    except json.JSONDecodeError as e:
                        print(f"Erro ao decodificar JSON: {e}")
                        time.sleep(60)
                        continue

                print(f"Conteúdo do JSON carregado: {dados}")

                if not isinstance(dados, list):
                    print("Erro: JSON deve conter uma lista de objetos.")
                    time.sleep(60)
                    continue

                print("Resetando 'enviado' para False...")

                for item in dados:
                    print(f"Processando item: {item}")
                    if isinstance(item, dict) and "enviado" in item:
                        item["enviado"] = False  

                print("Salvando o JSON atualizado...")

                with open(arquivo, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)

                print("Todos os agendamentos foram resetados!")

            except Exception as e:
                print(f"Erro inesperado: {e}")

            time.sleep(86400)  # Espera mais um dia antes de rodar novamente

    thread = threading.Thread(target=resetar, daemon=True)
    thread.start()
    

