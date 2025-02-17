import json
import uuid
from pathlib import Path

from assets.func.uteis.popUp import popUp
from assets.func.login.uteis.tratar_entradas_criar_usuario import tratar_entradas_criar_usuario

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap"
base_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

# Define o caminho do arquivo de usuários
ARQUIVO_USUARIOS = base_dir / ".usuarios.json"

def criar_usuario(
        raw_usuario,
        raw_senha, 
        raw_confirmar_senha,
        raw_email,
        raw_confirmar_email,
        raw_telefone,
        raw_confirmar_telefone):  
 
    id_unico = uuid.uuid4()

    entrada_tratada = tratar_entradas_criar_usuario(
        raw_usuario, 
        raw_senha, raw_confirmar_senha,
        raw_email, raw_confirmar_email, 
        raw_telefone, raw_confirmar_telefone)
    
    if entrada_tratada:
        usuario = {
            "id": str(id_unico),
            "usuario": str(raw_usuario).strip().upper(),
            "senha": str(raw_senha),
            "email": str(raw_email),
            "telefone": str(raw_telefone),
            "status": True  # Simula a ação de deletar quando False
        }

        try:
            with ARQUIVO_USUARIOS.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        except FileNotFoundError:
            usuarios = []

        usuarios.append(usuario)

        with ARQUIVO_USUARIOS.open("w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4)

        popUp('Cadastro criado com sucesso!')
        return True
