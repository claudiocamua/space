Alura Space

Alura Space é uma aplicação web desenvolvida durante a formação Django: Crie aplicações em Python da Alura. O projeto permite que usuários se cadastrem, façam login e interajam com a plataforma de forma dinâmica.

Funcionalidades

Cadastro de usuários

Login e logout

Interface interativa com Django templates

Gestão de conteúdo com Django models

Aplicação de boas práticas de desenvolvimento web com Python e Django

Tecnologias Utilizadas

Python 3.x

Django

HTML, CSS

SQLite (banco de dados padrão do Django)

Instalação

Clone o repositório:

git clone https://github.com/claudiocamua/space.git


Entre na pasta do projeto:

cd space


Crie um ambiente virtual:

python -m venv venv


Ative o ambiente virtual:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Execute as migrações do banco de dados:

python manage.py migrate


Crie um superusuário (opcional, para acesso administrativo):

python manage.py createsuperuser


Execute o servidor de desenvolvimento:

python manage.py runserver


Acesse a aplicação no navegador:

http://127.0.0.1:8000
