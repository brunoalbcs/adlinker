from pydantic import BaseModel, HttpUrl


# Request (o que vem do cliente)
class LinkRequest(BaseModel):
    link: HttpUrl  # verifica automaticamente se é um link válido
    #codigo: str | essa parte vai existir apenas se eu permitir que o usuário escolha o próprio link encurtado.

# Response (o que vai ser enviado para o cliente)
class LinkResponse(BaseModel):
    link_original: HttpUrl
    link_encurtado: str



