# MovieLens Recommender System

## Como rodar

```bash
docker-compose up --build
```

Acesse a documentação Swagger em: http://localhost:8000/docs

## Endpoint disponível

- `GET /recommend/{user_id}`

Retorna 5 recomendações de filmes para o usuário fornecido.