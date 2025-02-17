import json
from assets.func.uteis.popUp import popUp
from assets.func.planilha.info_planilha.info_planilha import info_planilha
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()
dados_contatos = []

def definir_origem(excel, pagina_excel, agenda):
    global dados_contatos
    if excel:
        try:
            sheet = info_planilha(pagina_excel)
            if not sheet:
                return []
        except:
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

        except:
            popUp("Nenhuma planilha selecionada")
            return []

        return dados_contatos  # Retorna a lista de dicionários, não mais json.dumps()

    elif agenda:
        caminho_agenda = f"assets/arquivos/contatos/{usuario_id}.json"
        with open(caminho_agenda, "r", encoding="utf-8") as f:
            contatos = json.load(f)
        dados_contatos = [contato for contato in contatos if contato.get("enviar")]

        return dados_contatos
