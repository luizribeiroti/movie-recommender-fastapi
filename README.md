# MovieLens Recommender System

Este projeto implementa um sistema de recomendação de filmes usando o conjunto de dados [MovieLens (ml-latest-small)](https://grouplens.org/datasets/movielens/), com uma API desenvolvida em **FastAPI** e executada em **Docker**.

---

## Tecnologias utilizadas

- Python 3.11
- FastAPI
- Docker / Docker Compose
- pandas, numpy, scikit-learn
- Swagger UI (documentação automática)

---

## Como rodar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Execute com Docker
bash
Copiar
Editar
docker-compose up --build
3. Acesse a API
Documentação interativa Swagger:
http://localhost:8000/docs

Funcionalidade
Endpoint disponível
Método	URL	Descrição
GET	/recommend/{user_id}	Retorna 5 recomendações de filmes para o usuário informado

Exemplo:

bash
Copiar
Editar
GET http://localhost:8000/recommend/1
Modelo de Recomendação
O sistema utiliza filtragem colaborativa baseada em similaridade de usuários. A lógica é:

Constrói uma matriz usuário x filme a partir do ratings.csv

Calcula a similaridade entre usuários com cosine_similarity

Gera recomendações com base nas avaliações dos usuários mais semelhantes

Este método não depende de conteúdo textual dos filmes, apenas do comportamento dos usuários.

 Estrutura do Projeto
bash
Copiar
Editar
recommender_ml_small/
├── app/
│   ├── main.py             # API FastAPI
│   ├── model.py            # Lógica da recomendação
│   ├── data_loader.py      # Leitura dos arquivos CSV
│   └── data/
│       ├── movies.csv      # Dados de filmes
│       └── ratings.csv     # Dados de avaliações
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── start.bat / start.sh
└── README.md
Testes e melhorias
Pronto para receber testes com pytest

Pode ser expandido com:

Banco de dados (PostgreSQL, MongoDB)

Filtro por gênero, tags ou conteúdo (modelo híbrido)

Autenticação de usuários

 Observações
Este projeto foi desenvolvido como atividade prática para demonstrar a construção de um sistema de recomendação moderno, usando ferramentas reais de mercado como FastAPI e Docker.

 Autor
Luiz Ribeiro