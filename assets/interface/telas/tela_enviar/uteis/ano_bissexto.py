from datetime import datetime


def ano_bissexto():
    ano = datetime.now().year
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

