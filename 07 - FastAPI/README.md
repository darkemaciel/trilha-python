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
render.yaml   # Blueprint do Render (web service + banco Postgres)
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

## Deploy no Render

O deploy usa o Blueprint (`render.yaml`) deste diretório, que provisiona automaticamente:

- um **Web Service** (Docker) rodando esta API;
- um banco **Postgres** (`fastapi-crud-db`), com a `DATABASE_URL` já conectada ao Web Service via `fromDatabase`.

Como este repositório é um monorepo (a raiz não é este projeto), o `render.yaml` não fica na raiz do repo — ele usa a chave `rootDir` para apontar para esta subpasta (`07 - FastAPI`), e os demais caminhos (`dockerfilePath`) são relativos a ela.

Passos para configurar (uma vez só):

1. No dashboard do Render: **New → Blueprint**, selecione este repositório.
2. No campo **Blueprint Path**, informe:
   ```
   07 - FastAPI/render.yaml
   ```
3. Confirme a criação — o Render vai propor o Web Service e o banco Postgres para aprovação.

Depois disso, qualquer push no `main` (ou "Sync Blueprint"/"Manual Deploy" no dashboard) atualiza o serviço.

**Atenção:** se `DATABASE_URL` não estiver definida (ex.: Blueprint mal configurado), a API sobe normalmente, só que gravando num SQLite dentro do container — sem erro nenhum, mas os dados somem a cada novo deploy. Pra confirmar que está gravando no Postgres de verdade, crie um item via `/docs`, force um redeploy e confira se ele continua lá.
