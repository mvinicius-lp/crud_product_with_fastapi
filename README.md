# FastAPI CRUD de Produtos

Este projeto é uma API RESTful para gerenciamento de produtos, construída com FastAPI e SQLModel. Ele permite criar, ler, atualizar e excluir produtos em um banco de dados SQLite.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados antes de executar o projeto:

- Python 3.10+
- SQLite (já incluído no Python)
- `pip` para gerenciamento de pacotes
- Arquivo `.env` contendo a variável `DATABASE_URL`

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e defina a variável `DATABASE_URL`, por exemplo:
   ```env
   DATABASE_URL=sqlite:///database.db
   ```

## Estrutura do Projeto

```
📂 projeto
│-- 📂 models
│   ├── product.py
│-- 📂 routes
│   ├── home.py
│   ├── product.py
│-- database.py
│-- main.py
│-- requirements.txt
│-- .env
│-- README.md
```

### `main.py`
Arquivo principal que inicia a aplicação FastAPI e inclui os roteadores das rotas `home` e `products`.

### `database.py`
Gerencia a conexão com o banco de dados usando SQLModel e SQLite. Ele:
- Cria a conexão com o banco de dados a partir da variável `DATABASE_URL`
- Configura a criação automática de tabelas
- Habilita `PRAGMA foreign_keys=ON` para o SQLite

### `models/product.py`
Define o modelo `Product` usando SQLModel:
- `id`: Chave primária
- `name`: Nome do produto
- `price`: Preço do produto
- `date_fab`: Data de fabricação (valor padrão: data e hora atuais)
- `date_val`: Data de validade (valor padrão: data e hora atuais)
- `cod`: Código do produto

### `routes/home.py`
Fornece uma rota raiz (`/`) que retorna uma mensagem de boas-vindas.

### `routes/product.py`
Implementa as operações CRUD para os produtos:
- `POST /products/` – Cria um novo produto
- `GET /products/` – Obtém a lista de produtos com paginação
- `PUT /products/{product_id}` – Atualiza um produto existente
- `DELETE /products/{product_id}` – Exclui um produto

## Executando o Projeto

1. Certifique-se de que seu ambiente virtual está ativado.
2. Execute o servidor FastAPI:
   ```sh
   uvicorn main:app --reload
   ou
   fastapi dev main.py
   ```
3. Acesse a documentação interativa no navegador:
   - OpenAPI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Logs e Debugging
O projeto usa logging para depuração do SQLAlchemy. Para visualizar logs SQL, altere o nível de log conforme necessário em `database.py`.

## Melhorias Futuras
- Adicionar autenticação e autorização
- Suporte para PostgreSQL ou MySQL
- Testes automatizados com `pytest`
- Validação de entrada mais robusta

## Licença
Este projeto está sob a licença MIT.

