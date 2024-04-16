# API de Gerenciamento de Usuários

Esta é uma API simples para gerenciar uma lista de usuários. Ela permite realizar operações CRUD (Create, Read, Update, Delete) para manipular os dados dos usuários.

## Funcionalidades Principais

- **Obter todos os usuários**: Retorna uma lista de todos os usuários cadastrados.
- **Obter um usuário específico pelo ID**: Retorna os detalhes de um usuário com base no seu ID.
- **Adicionar um novo usuário**: Permite adicionar um novo usuário à lista.
- **Atualizar um usuário existente**: Permite atualizar os detalhes de um usuário existente.
- **Excluir um usuário existente**: Permite excluir um usuário da lista.

## Rotas Disponíveis

```http
GET /users
GET /users/{id}
POST /users
PUT /users/{id}
DELETE /users/{id}
```

## Parâmetros

### Usuário

- **id** (int): O identificador único do usuário.
- **name** (string): O nome do usuário.
- **age** (int, opcional): A idade do usuário.
- **email** (string, opcional): O endereço de e-mail do usuário.

## Exemplo de Uso

### Adicionar um Novo Usuário

```http
POST http://localhost:5000/users
Content-Type: application/json

{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}
```

## Como Usar

Você pode usar esta API para criar, visualizar, atualizar e excluir usuários em uma aplicação web ou móvel. Basta enviar requisições HTTP para as rotas correspondentes para realizar as operações desejadas.

## Executando Localmente

Para executar esta API localmente, siga estas etapas:

1. Clone este repositório para o seu ambiente de desenvolvimento:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd nome-do-repositorio
```

3. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor da API:

```bash
python app.py
```

5. Acesse a API em `http://localhost:5000`.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request com melhorias.
