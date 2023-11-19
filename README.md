# Projeto para a Universidade Federal do Ceará para alocação de professores

## Descrição
É um projeto de alocação de professores e verificação de integridade de horários e salas, utilizando Vue para front-end e Django para back-end com a solução de banco de dados integrada.

## Tecnologias Utilizadas
- Vue: Linguagem de programação usada para front-end.
- Django: Framework com linguagem nativa python para back-end.
## Instalação
### Pré-requisitos

- Node.js e npm (para Vue.js)
- Python (para Django)

### Configurando o Ambiente Django

1. Instale o Django:
   ```bash
   
   pip install django
Crie um novo projeto Django:

bash
Copy code
django-admin startproject nome_do_projeto_django
Navegue até o diretório do projeto Django:

  ```bash

    cd djangoProject
  ```

Crie um novo app Django (se necessário):

Execute o migrate 
```
python manage.py migrate
```
Inicie o servidor Django para testar:

``` 
python manage.py runserver
```
Acesse http://localhost:8000.

Configurando o Projeto Vue.js
Instale o Vue CLI (se ainda não estiver instalado):

```
npm install -g @vue/cli
```
Inicie o servidor de desenvolvimento Vue:

```
npm run serve
```
Acesse http://localhost:8080.

Integrando Django e Vue.js
Instale pacotes de CORS no Django:
```
pip install django-cors-headers
```
