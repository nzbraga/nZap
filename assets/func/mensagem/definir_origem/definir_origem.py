import json
from pathlib import Path
from assets.func.uteis.popUp import popUp
from assets.func.planilha.info_planilha.info_planilha import info_planilha
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()
dados_contatos = []

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap" / "contatos"
base_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

def definir_origem(excel, pagina_excel, agenda):
    print(f'excel{excel}\npagina_excel{pagina_excel}\nagenda{agenda}')
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
            header = [cell.value for cell in sheet[1]]  # Captura os nomes das colunas
            dados_contatos = []

            for row in sheet.iter_rows(min_row=2, values_only=True):
                row_dict = dict(zip(header, row))  # Transforma a linha em um dicionário

                if row_dict.get("nome") is None or row_dict["nome"] == "":
                    break

                raw_numero = row_dict.get("telefone")  # Altere conforme o nome real da coluna
                raw_nome = row_dict.get("nome")
                aniversario = row_dict.get("aniversario")

                dados_contatos.append({
                    "nome": raw_nome,
                    "telefone": raw_numero,
                    "aniversario": aniversario
                })

        except Exception:
            popUp("Nenhuma planilha selecionada")
            return []

        return dados_contatos  # Retorna a lista de dicionários, não mais json.dumps()

    elif agenda:
        caminho_agenda = base_dir / f".{usuario_id}.json"
        print(f'caminho agenda{caminho_agenda}')
        try:
            with caminho_agenda.open("r", encoding="utf-8") as f:
                contatos = json.load(f)
            dados_contatos = [contato for contato in contatos if contato.get("enviar")]
            
            return dados_contatos
        except FileNotFoundError:
            popUp("Nenhum contato encontrado.")
            return []
