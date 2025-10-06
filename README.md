# Recipes
🎉 Projeto em Python e Django - Web Service para publicação de receitas gastonômicas.



comandos básicos
pip show python-decouple
pip show python pymysql
pip install python-decouple
pip install python pymysql


## Configuração do arquivo .env
#### Banco de Dados
DB_NAME = ""
#### Usuário
DB_USER = ""
#### Senha
DB_PASSWORD = ""
#### Domínio
DB_HOST = ""
#### Porta
DB_PORT = ""

## Configuração do arquivo settings.py

#### Ativa o Mysql
import pymysql
pymysql.install_as_MySQLdb()

#### Configuração de Banco
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='3306')
    }
}
