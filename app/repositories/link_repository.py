from sqlalchemy.orm import Session
from app.models import Link

def buscar_codigo(db: Session, codigo: str):
    result = db.query(Link).filter(Link.link_curto == codigo).first()
    return result

def buscar_link_original(db: Session, link: str):
    result = db.query(Link).filter(Link.link_original == link).first()
    return result

def salvar_link(db: Session, link_original: str, codigo: str):
    link = Link(link_original=link_original, link_curto=codigo)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


