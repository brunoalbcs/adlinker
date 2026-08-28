from fastapi import FastAPI
from app.routers import link_router
from app.database import Base, engine
import app.models  # É obrigatório importar os models aqui para o SQLAlchemy enxergar a tabela

# 1. O GATILHO DO BANCO DE DADOS
# Essa linha mágica vai no PostgreSQL e cria a tabela 'links' automaticamente se ela não existir
Base.metadata.create_all(bind=engine)

# 2. INICIALIZAÇÃO DA API
app = FastAPI(title="AdLinker API - Arquitetura em Camadas")

# 3. PLUGANDO AS ROTAS (O Roteador)
app.include_router(link_router.router)