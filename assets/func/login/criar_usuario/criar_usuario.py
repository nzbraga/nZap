import json
import uuid

from assets.func.uteis.popUp import popUp
from assets.func.login.uteis.tratar_entradas_criar_usuario import tratar_entradas_criar_usuario


ARQUIVO_USUARIOS = "./assets/arquivos/usuarios/.usuarios.json"

def criar_usuario(
        raw_usuario,
        raw_senha, 
        raw_confirmar_senha,
        raw_email,
        raw_confirmar_email,
        raw_telefone,
        raw_confirmar_telefone,):  
 
    id_unico = uuid.uuid4()

    entrata_tratada = tratar_entradas_criar_usuario(
        raw_usuario, 
        raw_senha, raw_confirmar_senha,
        raw_email, raw_confirmar_email, 
        raw_telefone, raw_confirmar_telefone)
    
    if entrata_tratada:
        usuario = {
            "id": str(id_unico),
            "usuario": str(raw_usuario).strip().upper(),
            "senha": str(raw_senha),
            "email": str(raw_email),
            "telefone": str(raw_telefone),
            "status": True #simula a açao de deletar quando false
        }

        try:
            with open(ARQUIVO_USUARIOS, "r") as f:
                usuarios = json.load(f)
            popUp('Cadastro criado com Sucesso!')
            return True
        

        except FileNotFoundError:
            usuarios = []
    
        usuarios.append(usuario)
        
        with open(ARQUIVO_USUARIOS, "w") as f:
            json.dump(usuarios, f, indent=4)