from assets.func.uteis.popUp import popUp

def logar(usuario, senha):
    if not usuario:
        popUp("Atencao", "Usuario nao informado")
    elif usuario:
        popUp(f'Bem vindo {usuario.upper()}')
        popUp(f'Senha {senha}')
        #ela_messagem(usuario.upper())