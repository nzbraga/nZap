import json
from pathlib import Path

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap"
base_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

# Define os caminhos dos arquivos JSON
ARQUIVO_USUARIOS = base_dir / ".usuarios.json"
ARQUIVO_SESSAO = base_dir / "sessao" / ".sessao.json"

def autenticar_login(raw_usuario, senha):
    usuario = raw_usuario.strip().upper()
    senha = senha.strip()  # Garantir que a senha também não tenha espaços extras
    print(f'{usuario}{senha}')
    try:
        with ARQUIVO_USUARIOS.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    print(f'>>>>>{data}')

    for user in data:
        print(f'user >>>>>{user}')
        if not user.get("status", True):  # Se status for False, negar login
            return False
        print(f'user: {user["usuario"]}, senha: {user["senha"]}')
        if user["usuario"] == usuario and user["senha"] == senha:
            # Criando sessão com ID e nome do usuário autenticado
            sessao = {"id": user["id"], "nome": user["usuario"]}
            with ARQUIVO_SESSAO.open("w", encoding="utf-8") as f:
                json.dump(sessao, f, indent=4)
            return True
    return False
