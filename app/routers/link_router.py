from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from app.schemas import LinkResponse, LinkRequest
from sqlalchemy.orm import Session
import app.services.link_service as ls
from app.database import get_db



router = APIRouter()

@router.post("/", response_model=LinkResponse)
def POST(link: LinkRequest, db: Session = Depends(get_db)):
    return ls.criar_link_encurtado(db, str(link.link), "http://127.0.0.1:8000/")

@router.get("/{codigo}")
def REDIRECT(codigo: str, db: Session = Depends(get_db)):
    link_original = ls.obter_link_original(db, codigo)
    if link_original is not None:
        return RedirectResponse(url=link_original)
    raise HTTPException(status_code=404, detail="Link não encontrado no servidor.")