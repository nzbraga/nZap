from assets.func.uteis.popUp import popUp
from assets.func.login.autenticar_login.autenticar_login import autenticar_login

def logar(usuario, senha):
    if not usuario or not senha:
        popUp("Usuario ou Senha nao informado")
    
    loged = autenticar_login(usuario, senha)

    if loged:
        return True
    else:
        popUp('Usuario ou Senha incorretos')