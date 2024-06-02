
# Installation

>### For run project you need installation __Git__, __Docker__ and __docker compose__ instruments.

How to install Docker - <https://docs.docker.com/engine/install/>

How to install docker-compose - <https://docs.docker.com/compose/install/>

How to install Git - <https://www.git-scm.com/downloads>

___
# Download project from GitHub

>### For download application use command in terminal
>``git clone https://github.com/denysyakymchuk/TestTaskLuna.git``


___
# Configuration

>### Create **.env** file in main directory of project. He has to contain variables:

| Postgresql        | Django                    |                            
|:------------------|:--------------------------|
| POSTGRES_NAME     | DJANGO_SUPERUSER_PASSWORD |                            
| POSTGRES_USER     | SECRET_KEY                | 
| POSTGRES_PASSWORD | DJANGO_SUPERUSER_USERNAME |     
| POSTGRES_DB       | DJANGO_SUPERUSER_EMAIL    |                           
| POSTGRES_HOST     |                           |                            
| POSTGRES_PORT     |                           |                            


___
# Run application

>### In terminal go to main directory and type command
> ``docker compose up --build``
> 
> Then application will available on [http://localhost:8000/](http://localhost:8000/)
> 
> Documentation API - [http://localhost:8000/swagger/](http://localhost:8000/swagger/) 