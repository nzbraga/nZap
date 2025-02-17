from assets.func.uteis.popUp import popUp
from assets.func.planilha.info_planilha.info_planilha import info_planilha
def definir_origem(excel, pagina_excel, agenda):
    if excel:
        try:
            sheet = info_planilha(pagina_excel)
            if not sheet:
                return
        except:
            #print('Erro ao ler planilha')
            popUp('Erro ao ler planilha')

        try:
            for row in sheet.iter_rows(min_row=2):
                
                raw_number = row[0].value
                raw_name = row[1].value
                birthDay = row[2].value

                print(f'numero: {raw_number}\nnome:{raw_name}\naniversario:{birthDay}')
        except:
            popUp("Nenhuma planilha selecionada")
        
        return "excel"
    elif agenda:

        return "agenda"
    