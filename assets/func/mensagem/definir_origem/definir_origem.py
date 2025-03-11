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
    global dados_contatos

    #print(f'origem: {excel}, {pagina_excel}, {agenda}')
    
    if excel:
        try:
            #print(f'pagina: {pagina_excel}')
            sheet = info_planilha(pagina_excel)
            #print(f'sheet: {sheet}')
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
                row_dict = {key: value for key, value in zip(header, row) if key is not None}  # Remove colunas sem nome
                
                
                if all(value is None or value == "" for value in row_dict.values()):
                    break

                dados_contatos.append(row_dict)

            print(f'contatos:-------------------------------------------- {dados_contatos}')
            return dados_contatos              
        
        
        except Exception:
            popUp("Erro ao processar os dados da planilha")
            return []
      

    elif agenda:
        caminho_agenda = base_dir / f".{usuario_id}.json"        
        try:
            with caminho_agenda.open("r", encoding="utf-8") as f:
                contatos = json.load(f)
            dados_contatos = [contato for contato in contatos if contato.get("enviar")]
            
            return dados_contatos
        except FileNotFoundError:
            popUp("Nenhum contato encontrado.")
            return []

    dados_contatos = []