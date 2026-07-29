# Jogoteca 🎮

Uma aplicação web para gerenciar sua coleção de jogos desenvolvida com Flask e MySQL.

## 📋 Descrição

Jogoteca é uma aplicação web que permite gerenciar informações sobre seus jogos. Você pode:

- **Listar** todos os seus jogos com detalhes (nome, categoria, console)
- **Adicionar** novos jogos à sua coleção
- **Editar** informações de jogos existentes
- **Deletar** jogos da sua coleção
- **Autenticar-se** para acessar funcionalidades de criação e edição
- **Gerenciar sessão** de usuário com login e logout

## 🛠️ Requisitos do Sistema

- **Python**: 3.12 ou superior
- **MySQL**: 8.0 ou superior
- **pip**: Gerenciador de pacotes Python

## 📦 Dependências

As dependências principais do projeto são:

- **Flask** (3.0.3) - Framework web
- **Flask-SQLAlchemy** (3.1.1) - ORM para banco de dados
- **SQLAlchemy** (2.0.32) - SQL toolkit
- **mysql-connector-python** (9.0.0) - Driver MySQL

Para ver todas as dependências, consulte `requirements.txt`.

## 🚀 Instalação

### 1. Clone ou acesse o diretório do projeto

```bash
cd /caminho/para/jogoteca
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ative o ambiente virtual

**No macOS/Linux:**
```bash
source .venv/bin/activate
```

**No Windows:**
```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure o banco de dados

O banco de dados `jogoteca` já deve estar criado. Se não estiver, crie com:

```bash
mysql -u root -padmin -e "CREATE DATABASE jogoteca;"
```

### 6. Configure as credenciais (se necessário)

Edite o arquivo `config.py` e ajuste as credenciais MySQL:

```python
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{pwd}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='seu_usuario',
        pwd='sua_senha',
        server='localhost',
        database='jogoteca'
    )
```

## 🎯 Uso

### Iniciar a aplicação

```bash
python jogoteca.py
```

A aplicação estará disponível em: **http://localhost:5000**

### Navegação

1. **Página Inicial** (`/`) - Lista todos os jogos
2. **Novo Jogo** (`/novo`) - Formulário para adicionar um jogo (requer login)
3. **Editar Jogo** (`/editar/<id>`) - Formulário para editar um jogo (requer login)
4. **Deletar Jogo** (`/deletar/<id>`) - Remove um jogo da lista (requer login)
5. **Login** (`/login`) - Autenticação de usuário
6. **Logout** (`/logout`) - Encerrar sessão

## 📊 Estrutura do Banco de Dados

### Tabela: `jogos`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Identificador único (chave primária) |
| nome | VARCHAR(50) | Nome do jogo |
| categoria | VARCHAR(40) | Categoria do jogo |
| console | VARCHAR(20) | Console onde o jogo é jogado |

### Tabela: `usuarios`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| nickname | VARCHAR(8) | Apelido único do usuário (chave primária) |
| nome | VARCHAR(20) | Nome completo do usuário |
| senha | VARCHAR(100) | Senha do usuário |

## 📁 Estrutura do Projeto

```
jogoteca/
├── jogoteca.py           # Arquivo principal da aplicação Flask
├── config.py             # Configurações da aplicação
├── models.py             # Modelos de banco de dados (Jogos, Usuarios)
├── views.py              # Rotas e controllers
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
├── .venv/                # Ambiente virtual Python
├── static/               # Arquivos estáticos (CSS, JS, imagens)
└── templates/            # Templates HTML
    ├── template.html     # Template base
    ├── list.html         # Página de listagem de jogos
    ├── new.html          # Formulário de novo jogo
    ├── edit.html         # Formulário de edição de jogo
    └── login.html        # Página de login
```

## 🔐 Segurança

⚠️ **Nota Importante**: Esta é uma aplicação de demonstração. Para uso em produção:

- Implemente hash de senha (use bibliotecas como `bcrypt` ou `werkzeug.security`)
- Configure variáveis de ambiente para credenciais sensíveis
- Use HTTPS em vez de HTTP
- Implemente proteção CSRF
- Valide e sanitize todas as entradas do usuário

## 🐛 Troubleshooting

### Erro: "Access denied for user 'root'@'localhost'"

Verifique se o MySQL está rodando e se as credenciais em `config.py` estão corretas:

```bash
mysql -u root -padmin -e "SELECT 1;"
```

### Erro: "No module named 'flask'"

Certifique-se de que o ambiente virtual está ativado:

```bash
source .venv/bin/activate  # macOS/Linux
```

### Erro: "Database 'jogoteca' doesn't exist"

Crie o banco de dados:

```bash
mysql -u root -padmin -e "CREATE DATABASE jogoteca;"
```

## 📝 Licença

Este é um projeto de aprendizado. Use livremente para fins educacionais.

## 👨‍💻 Autor

Desenvolvido por Rangel Gonçalves como um projeto de aprendizado Flask e MySQL.

---

**Última atualização**: 29 de julho de 2026
