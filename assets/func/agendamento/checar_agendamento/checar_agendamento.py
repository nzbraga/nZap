import threading
import time
import json
from datetime import datetime
from pathlib import Path
import traceback

from assets.func.mensagem.montar_msg.enviar_msg import enviar_msg
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.sessao.sessao import sessao_id
from assets.func.config.abrir_config import abrir_config

usuario_id = sessao_id()
base_dir = Path.home() / "nZap"
agendado_dir = base_dir / "agendados"
ARQUIVO_AGENDADO = agendado_dir / f".{usuario_id}.json"

# Controladores de execução
agendamento_thread = None
stop_event = threading.Event()


def checar_agendamentos(arquivo, stop_event):
    while not stop_event.is_set():
        try:
            hora_atual = datetime.now().hour
            config = abrir_config(usuario_id)
            remetente = config.get("remetente")
            primeira_hora = config.get("primeira_hora")
            ultima_hora = config.get("ultima_hora")
            intervalo_envio = config.get("intervalo_envio")

            if hora_atual < primeira_hora or hora_atual >= ultima_hora:
                print(f"Fora do horário de execução ({primeira_hora}h até {ultima_hora}h). Aguardando...")
                time.sleep(10)
                continue

            if not arquivo.exists():
                print("Arquivo não encontrado.")
                time.sleep(10)
                continue

            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            for item in dados:
                if stop_event.is_set():
                    return  # Encerra rapidamente se for pedido

                contato = item["contato"]
                mensagem = item["mensagem"].replace("/n", "\n").replace("\\n", "\n")
                frequencia = item["frequencia"]
                enviado = item["enviado"]

                hoje = datetime.now()

                if frequencia in ["vencimento", "mensal"] and not enviado:
                    if contato.get(frequencia) == hoje.strftime("%d"):
                        item["enviado"] = True
                        enviar_msg([contato], mensagem)

                elif frequencia == "aniversario" and not enviado:
                    if contato.get(frequencia) == hoje.strftime("%d-%m"):
                        item["enviado"] = True
                        enviar_msg([contato], mensagem)

                elif frequencia == "semanal" and not enviado:
                    if contato.get(frequencia) == hoje.weekday():
                        item["enviado"] = True
                        enviar_msg([contato], mensagem)

                with open(arquivo, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)

            time.sleep(10)
            
            enviar_mensagem("Agendamento: Processo concluído.", remetente, "Verificação concluída.")

        except Exception:
            traceback.print_exc()

        intervalo = intervalo_envio * 3600
        print(f"Aguardando {intervalo} segundos...")
        for _ in range(int(intervalo / 5)):
            if stop_event.is_set():
                return
            time.sleep(5)


def iniciar_checar_agendamentos():
    global agendamento_thread, stop_event

    if agendamento_thread and agendamento_thread.is_alive():
        print("Parando execução anterior...")
        stop_event.set()
        agendamento_thread.join()

    print("Iniciando nova execução de checagem de agendamentos...")
    stop_event = threading.Event()
    agendamento_thread = threading.Thread(target=checar_agendamentos, args=(ARQUIVO_AGENDADO, stop_event))
    agendamento_thread.start()
