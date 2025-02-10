from assets.func.sessao.sessao import sessao_id
def checar_logado():
    usuario_id = sessao_id()    
    if usuario_id:
        return usuario_id
    else:
        return False