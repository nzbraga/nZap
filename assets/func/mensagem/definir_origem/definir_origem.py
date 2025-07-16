import json
from pathlib import Path
from assets.func.uteis.popUp import popUp
from assets.func.planilha.info_planilha.info_planilha import info_planilha
from assets.func.sessao.sessao import sessao_id
import re  # Para limpar caracteres não numéricos

usuario_id = sessao_id()
dados_contatos = []

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap" / "contatos"
base_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

def definir_origem(excel, pagina_excel, agenda):    
    global dados_contatos

    if excel:
        try:
            sheet = info_planilha(pagina_excel)
            if not sheet:
                return []
        except Exception:
            popUp('Erro ao ler planilha')
            return []

        try:
            # Captura os nomes das colunas
            header = [cell.value for cell in sheet[1]]  
            dados_contatos = []

            for row in sheet.iter_rows(min_row=2, values_only=True):
                row_dict = {}

                for key, value in zip(header, row):
                    if key is None:
                        continue

                    # Normaliza o nome da coluna
                    coluna = key.strip().lower()

                    # Ajuste para telefone/celular
                    if coluna in ["telefone", "celular"]:
                        coluna = "contato"  # Renomeia para "contato"
                        if value:
                            # Remove todos os caracteres que não sejam números
                            value = re.sub(r"\D", "", str(value)).strip()
                            if value == "":
                                value = None  # Se ficou vazio depois da limpeza, considera como None

                    # Ajuste para datas
                    if coluna in ["aniversario", "vencimento", "data"]:
                        if value:
                            value = str(value).replace("/", "-").strip()

                    row_dict[coluna] = value

                # Verifica se a linha inteira está vazia
                if all(v is None or v == "" for v in row_dict.values()):
                    break

                dados_contatos.append(row_dict)

            return dados_contatos              
        
        except Exception:
            popUp("Erro ao processar os dados da planilha")
            return []

    elif agenda:
        print('em desenvolvimento...')

    dados_contatos = []
