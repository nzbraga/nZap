import calendar
import locale
import datetime

# Define o local como pt_BR
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
number_month = current_month if current_month < 12 else 1
month = calendar.month_name[number_month]

#verifica se a hora eh maior que 22 ou menor que 6
def checar_hora(hour):
    if hour >= 22 or hour < 6:
        new_hour =6
        return new_hour
    else:
        return hour

def pegar_hora():
    hour = checar_hora(datetime.datetime.now().hour)
    minute = datetime.datetime.now().minute
    return (hour, minute)


def definir_saudacao(name='"Nome_do_Contato"'):
    hour, minute = pegar_hora()
    if hour >= 6 and hour <12:
        greeting = f'Bom dia {name},'
        return  greeting
    elif hour >= 12 and hour < 18:
        greeting = f'Boa Tarde {name},'
        return  greeting
    elif hour >= 18 and hour < 22:
        greeting = f'Boa Noite {name},'
        return  greeting


