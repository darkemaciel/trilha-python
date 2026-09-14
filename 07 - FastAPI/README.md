# 07 - FastAPI

API de estudo com CRUD de itens, construída com FastAPI e SQLAlchemy. Faz parte da trilha de estudos Python.

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- SQLite (padrão local) / PostgreSQL (produção, via `DATABASE_URL`)
- [uv](https://docs.astral.sh/uv/) para gerenciamento de dependências

## Estrutura do projeto

```
main.py       # instância do FastAPI e rotas do CRUD
models.py     # modelo SQLAlchemy (tabela `itens`)
schema.py     # schemas Pydantic (ItemBase, ItemCreate, Item)
database.py   # configuração da engine/sessão e dependência get_db
Dockerfile    # imagem para deploy (Render)
```

## Como rodar localmente

Pré-requisito: [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado.

```bash
uv sync
uv run uvicorn main:app --reload
```

A API sobe em `http://127.0.0.1:8000`. Documentação interativa (Swagger) em `http://127.0.0.1:8000/docs`.

Por padrão, os dados são gravados em um banco SQLite local (`test.db`). Para usar outro banco (ex.: PostgreSQL), defina a variável de ambiente `DATABASE_URL`.

## Endpoints

| Método | Rota            | Descrição                     |
|--------|-----------------|--------------------------------|
| GET    | `/`             | Mensagem de boas-vindas        |
| POST   | `/items/`       | Cria um item                   |
| GET    | `/itens/`       | Lista itens (com paginação)     |
| GET    | `/items/{id}`   | Busca um item pelo id           |
| PUT    | `/items/{id}`   | Atualiza um item pelo id        |
| DELETE | `/items/{id}`   | Remove um item pelo id          |

### Modelo de item

```json
{
  "id": 1,
  "name": "string",
  "price": 10.5,
  "is_offer": false
}
```

## Docker

```bash
docker build -t 07-fastapi .
docker run -p 8000:8000 07-fastapi
```

A porta é configurável via variável de ambiente `PORT` (padrão `8000`), usada pelo Render em deploy.
