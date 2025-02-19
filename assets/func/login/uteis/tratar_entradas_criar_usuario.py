import json
from pathlib import Path
from assets.func.uteis.popUp import popUp

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap"
base_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

# Define o caminho do arquivo de usuários
ARQUIVO_USUARIOS = base_dir / ".usuarios.json"

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
        return False  # Retorna False para indicar erro

    if senha != confirmar_senha:
        popUp("Senhas diferentes.") 
        return False
    
    if email != confirmar_email:
        popUp("emails diferentes.")
        return False

    if telefone != confirmar_telefone:
        popUp("Telefones diferentes.")
        return False
        
    try:
        if ARQUIVO_USUARIOS.exists():
            conteudo = ARQUIVO_USUARIOS.read_text(encoding="utf-8").strip()
            usuarios = json.loads(conteudo) if conteudo else []
        else:
            usuarios = []
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []  # Se der erro, assume uma lista vazia

    # Verifica se o usuário já existe
    if any(u["email"] == email for u in usuarios):
        popUp(f"Usuário com email: {email} já existe.")
        return False
    
    return True
