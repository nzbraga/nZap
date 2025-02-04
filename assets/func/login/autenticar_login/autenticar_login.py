import json

ARQUIVO_USUARIOS = "./assets/arquivos/.usuarios.json"

def autenticar_login(usuario, senha):
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    for user in data:
        if user["usuario"] == usuario and user["senha"] == senha:
            return True
    return False