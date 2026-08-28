from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from app.schemas import LinkResponse, LinkRequest
from sqlalchemy.orm import Session
import app.services.link_service as ls
from app.database import get_db



router = APIRouter()

@router.post("/", response_model=LinkResponse)
def POST(link: LinkRequest, request: Request, db: Session = Depends(get_db)):
    base_url = str(request.base_url)
    return ls.criar_link_encurtado(db, str(link.link), base_url)

@router.get("/{codigo}")
def REDIRECT(codigo: str, db: Session = Depends(get_db)):
    link_original = ls.obter_link_original(db, codigo)
    if link_original is not None:
        return RedirectResponse(url=link_original)
    raise HTTPException(status_code=404, detail="Link não encontrado no servidor.")