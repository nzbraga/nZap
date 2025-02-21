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
    print(f'excel: {excel}\npagina_excel: {pagina_excel}\nagenda: {agenda}')
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
                row_dict = dict(zip(header, row))
                
                if row_dict.get("nome") is None or row_dict["nome"] == "":
                    break

                dados_contatos.append(row_dict)
        except Exception:
            popUp("Erro ao processar os dados da planilha")
            return []

        return dados_contatos

    elif agenda:
        caminho_agenda = base_dir / f".{usuario_id}.json"
        print(f'caminho agenda: {caminho_agenda}')
        try:
            with caminho_agenda.open("r", encoding="utf-8") as f:
                contatos = json.load(f)
            dados_contatos = [contato for contato in contatos if contato.get("enviar")]
            
            return dados_contatos
        except FileNotFoundError:
            popUp("Nenhum contato encontrado.")
            return []
