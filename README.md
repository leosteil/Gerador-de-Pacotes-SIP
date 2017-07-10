# Gerador de Pacotes SIP - archivematica
Repositório usado para armazenar o trabalho final de disciplina de Bases da Gestão Eletrônica de Documentos.

O trabalho final de Disciplina de Bases da Gestão Eletrônica de Documentos teve como objetivo desenvolver um sistemas que fosse capaz de gerar Pacotes SIP que pudessem ser armazenados no repositório Archivematica. Os metadados utilizados foram os do padrão DublinCore com 15 campos.

O sistemas já pode ser usado, mas continua sendo desenvolvido usando o framework Django. Abaixo seguem algumas instruções para quem deseja utilizar o sistema de forma local. O desejo é que futuramente este projeto seja colocado online.

## Pacotes, libs e frameworks necessários

### Cliente MySQL
sudo apt-get install libmysqlclient-dev

### Cliente MySQL para Python 3
sudo pip3 install mysqlclient

### Django Framework (a versão utilizada no desenvolvimento foi a 1.10.5)
pip3 install Django

### Criar database nomeada como: "sipDB"

CREATE DATABASE sipDB;

Criar usuário "sip" com privilégios de root e password "root"

CREATE USER 'sip'@'localhost' IDENTIFIED BY 'root';

GRANT ALL PRIVILEGES ON *.* TO 'sip'@'localhost' WITH GRANT OPTION;

### Configuração do arquivo "settings.py" do projeto Django

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sipDB',
        'USER': 'sip',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



