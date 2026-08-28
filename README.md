# AdLinker 🔗

Um encurtador de links de alta performance construído com **Python** e **FastAPI**. 
O projeto foi desenvolvido utilizando a **Arquitetura em Camadas** (N-Tier Architecture), separando responsabilidades para garantir um código limpo, escalável e de fácil manutenção.

---

## 🌐 Teste Online
A API está hospedada na nuvem e pronta para testes:
* **Acesse a Documentação (Swagger UI):** [https://adlinker-api.onrender.com/docs](https://adlinker-api.onrender.com/docs)


---

## 🛠️ Tecnologias Utilizadas

*   **FastAPI:** Framework web moderno e rápido para construção da API.
*   **PostgreSQL:** Banco de dados relacional robusto.
*   **SQLAlchemy (ORM):** Mapeamento objeto-relacional para comunicação com o banco de dados.
*   **Pydantic:** Validação de dados rigorosa e serialização.
*   **Uvicorn:** Servidor web ASGI.
*   **Python-dotenv:** Gerenciamento de variáveis de ambiente.

## 🏗️ Arquitetura do Projeto

O projeto segue a divisão clássica de responsabilidades:
*   **Routers (Controllers):** Lida com as requisições HTTP e devolve as respostas.
*   **Services:** Contém a lógica e as regras de negócio da aplicação.
*   **Repositories:** Camada exclusiva para comunicação e execução de queries no banco de dados.
*   **Schemas:** Contratos de entrada (Request) e saída (Response) validados via Pydantic.
*   **Models:** Representação das tabelas do banco de dados.

## 🚀 Como executar o projeto localmente

### Pré-requisitos
*   Python 3.10+
*   PostgreSQL instalado e rodando.

### Passo a Passo

1. Clone o repositório:
git clone https://github.com/brunoalbcs/adlinker.git
cd adlinker

2. Crie e ative um ambiente virtual:
python -m venv venv
# No Windows: venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto e adicione sua string de conexão:
DATABASE_URL="postgresql://USUARIO:SENHA@localhost:5432/postgres"

5. Inicie o servidor local:
uvicorn app.main:app --reload

6. Acesse a documentação interativa (Swagger UI):
Abra o navegador em: http://127.0.0.1:8000/docs