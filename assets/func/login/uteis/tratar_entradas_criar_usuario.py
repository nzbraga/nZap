import json
from assets.func.uteis.popUp import popUp

ARQUIVO_USUARIOS = "./assets/arquivos/.usuarios.json"

def tratar_entradas_criar_usuario(
        usuario,
        senha, confirmar_senha, 
        email, confirmar_email,
        telefone, confirmar_telefone):
    
    if not all([
    usuario,
    senha,
    confirmar_senha,
    email,
    confirmar_email    
    ]):
        popUp("Campos obrigatorios não preenchidos.")

    if senha != confirmar_senha:
        popUp("Senhas diferentes.") 
    
    if email != confirmar_email:
        popUp("Emails diferentes.")

    if telefone:
        if telefone != confirmar_telefone:
            popUp("Telefones diferentes.")
        
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = []
   
     
    # Verifica se o usuário já existe
    if any(u["usuario"] == usuario["usuario"] for u in usuarios):
        print(f"Usuário {usuario['usuario']} já existe.")
        popUp(f"Usuário {usuario['usuario']} já existe.")
        return
    
    return True
    