from sqlalchemy.orm import Session
from app.schemas import LinkResponse
import app.repositories.link_repository as repo
import string
import random

def criar_link_encurtado(db: Session, link_original: str, base_url: str):
    # Verificar se o link já existe encurtado na base:
    # Remover essa parte caso habilite login para registro da quantidade de cliques no link curto do usuário.
    consulta = repo.buscar_link_original(db, link_original)
    if consulta:
        return {"link_original": link_original, "link_encurtado": base_url+consulta.link_curto}

    char = string.ascii_letters + string.digits
    codigo = "".join(random.choices(char, k=5))  # Cria um código de 5 dígitos
    while repo.buscar_codigo(db, codigo):
        codigo = "".join(random.choices(char, k=5))

    repo.salvar_link(db, link_original, codigo)

    return {"link_original": link_original, "link_encurtado": base_url+codigo}

def obter_link_original(db: Session, codigo: str):
    link = repo.buscar_codigo(db, codigo)
    if link:
        return link.link_original
    return None
