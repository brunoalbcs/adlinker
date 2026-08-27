from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import random
import string
app = FastAPI()

class Link(BaseModel):  # Request (o que vem do cliente)
    link: HttpUrl  # verifica automaticamente se é um link válido
    #curto: str | essa parte vai existir apenas se eu permitir que o usuário escolha o próprio link encurtado.

@app.get("/")
def get():
    return {"Encurtador de Links HTTP/HTTPS"}

database = {}
@app.post("/")
def encurtar(endereco: Link):

    # Verificar se o link já existe encurtado na base:
    # Remover essa parte caso habilite login para registro da quantidade de cliques no link curto do usuário.
    for codigo, link in database.items():
        if endereco.link == link:
            endereco_curto = f"http://127.0.0.1:8000/{codigo}"
            return {"link_original": endereco.link, "link_encurtado": endereco_curto}

    char = string.ascii_letters + string.digits
    codigo = "".join(random.choices(char, k=5))  # Cria um código de 5 dígitos
    while codigo in database:
        codigo = "".join(random.choices(char, k=5))

    database[codigo] = endereco.link  # Salva o redirecionamento no "banco de dados"

    endereco_curto = f"http://127.0.0.1:8000/{codigo}"
    return {"link_original": endereco.link, "link_encurtado": endereco_curto}

@app.get("/{codigo}")
def redirecionar(codigo: str):
    try:
        return RedirectResponse(database[codigo])
        # Se der algum problema depois, tenta mudar para str(database[codigo])
    except KeyError:
        raise HTTPException(status_code=404, detail="Link não encontrado no servidor.")