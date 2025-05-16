import json
from pathlib import Path

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap"
sessao_dir = base_dir / "sessao"
sessao_dir.mkdir(parents=True, exist_ok=True)  # Garante que a pasta "sessao" exista

# Define os caminhos dos arquivos JSON
ARQUIVO_USUARIOS = base_dir / ".usuarios.json"
ARQUIVO_SESSAO = sessao_dir / ".sessao.json"

def autenticar_login(raw_usuario, senha):
    usuario = raw_usuario.strip().upper()
    senha = senha.strip()  # Garantir que a senha também não tenha espaços extras
    
    try:
        with ARQUIVO_USUARIOS.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):  # Verifica se os dados são uma lista válida
                raise ValueError("Formato inválido no arquivo de usuários.")
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        data = []  # Se houver erro, assume que não há usuários cadastrados

    for user in data:
        if not user.get("status", True):  # Se status for False, negar login
            return False
        
        if user.get("usuario") == usuario and user.get("senha") == senha:
            sessao_dir.mkdir(parents=True, exist_ok=True)
            sessao = {"id": user.get("id", "desconhecido"), "nome": user.get("usuario", "desconhecido")}
            with ARQUIVO_SESSAO.open("w", encoding="utf-8") as f:
                print(f'arquivo criado na pasta{ARQUIVO_SESSAO} com sucesso.')
                json.dump(sessao, f, indent=4)
            return True
    
    return False
