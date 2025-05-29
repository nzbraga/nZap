import json
import time
from datetime import datetime
from pathlib import Path
import traceback

from assets.func.mensagem.montar_msg.enviar_msg import enviar_msg
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.sessao.sessao import sessao_id

base_dir = Path.home() / "nZap"
agendado_dir = base_dir / "agendados"

usuario_id = sessao_id()

ARQUIVO_AGENDADO = agendado_dir / f".{usuario_id}.json"

def checar_agendamentos(arquivo):
    while True:
        try:
            hora_atual = datetime.now().hour
            if hora_atual < 8 or hora_atual >= 18:
                print("Fora do horário de execução (08h às 18h). Aguardando...") 
                time.sleep(3600)
                continue

            print("Agendamoento: Verificando se o arquivo existe...")
            if not arquivo.exists():
                print("Arquivo não encontrado.")
                time.sleep(30)
                continue

            print("Agendamento: Arquivo encontrado! Lendo conteúdo...")

            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)


            #print(f"Conteúdo do JSON carregado: {dados}")

            for item in dados:


                # Extração de dados
                contato = item["contato"]     
                mensagem = item["mensagem"].replace("/n", "\n").replace("\\n", "\n")

     
                frequencia = item["frequencia"]
                enviado = item["enviado"]
                """
                filtrar as condicionais de envio aqui !!!
                """               
                if frequencia in ["vencimento", "mensal"] and enviado == False:

                    data_atual = datetime.now().strftime("%d")   

                    #print(f"contato vencimento: {contato.get(frequencia, 'Chave não encontrada')}\ndata atual: {data_atual}")   
                    if contato.get(frequencia) == data_atual: 
                        #print(f"enviando vencimento dia: {contato.get(frequencia, 'Chave não encontrada')}")
                        enviar_msg([contato], mensagem)

                        item["enviado"] = True

                elif frequencia == "aniversario" and enviado == False:

                    data_atual = datetime.now().strftime("%d-%m")   

                    #print(f"contato aniversario: {contato.get(frequencia, 'Chave não encontrada')}\ndata atual: {data_atual}")   
                    if contato.get(frequencia) == data_atual: 
                        print(f"enviando aniversario dia: {contato.get(frequencia, 'Chave não encontrada')}")
                        enviar_msg([contato], mensagem)

                        item["enviado"] = True
                
                elif frequencia == 'semanal' and enviado == False:
                    data_atual = datetime.today().weekday()
                    print(f"dia da semana: {data_atual}")
                    """
                    if contato.get(frequencia) == data_atual:  
                         enviar_msg([contato], mensagem)

                         item["enviado"] = True
                    """

            # Salvando o JSON atualizado
            print("Agendamoento: Salvando o JSON atualizado...")
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)

           
            print("Agendamento: Processo concluído.")
            enviar_mensagem("Agendamento: Processo concluído.", "21997633265", "Verificação de mensagem agendadas: Processo concluído.")

        except Exception as e:
            print("Agendamoento: Erro ao ler ou atualizar o arquivo JSON:")
            traceback.print_exc()


        time.sleep(21600)  # Espera 6 hora antes de verificar novamente
        #time.sleep(30)  
    