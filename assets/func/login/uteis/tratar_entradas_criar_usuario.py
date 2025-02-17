import json
from assets.func.uteis.popUp import popUp

ARQUIVO_USUARIOS = "./assets/arquivos/usuarios/.usuarios.json"

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
        popUp("Campos obrigatórios não preenchidos.")
        return  # Adicionado return para evitar continuar o código

    if senha != confirmar_senha:
        popUp("Senhas diferentes.") 
        return
    
    if email != confirmar_email:
        popUp("Emails diferentes.")
        return

    if telefone != confirmar_telefone:
        popUp("telefones diferentes.")
        return
        
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            conteudo = f.read().strip()
            if not conteudo:  # Se o arquivo estiver vazio
                usuarios = []
            else:
                usuarios = json.loads(conteudo)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []  # Se der erro, assume uma lista vazia


    # Verifica se o usuário já existe
    if any(u["email"] == email for u in usuarios):
        popUp(f"Usuário com email: {email} já existe.")
        return
    
    return True
