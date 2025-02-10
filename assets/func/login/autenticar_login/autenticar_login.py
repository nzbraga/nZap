import json

ARQUIVO_USUARIOS = "./assets/arquivos/usuarios/.usuarios.json"
ARQUIVO_SESSAO = "./assets/arquivos/sessao/.sessao.json"

def autenticar_login(raw_usuario, senha):
    usuario = raw_usuario.strip().upper()
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    for user in data:
        if user["usuario"] == usuario and user["senha"] == senha:
            # Criando sessão com ID e nome do usuário autenticado
            sessao = {"id": user["id"], "nome": user["usuario"]}
            with open(ARQUIVO_SESSAO, "w") as f:
                json.dump(sessao, f, indent=4)
            return True
    return False
