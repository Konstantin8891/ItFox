# ItFox

## Описание

API для постинга новостей, комментариев, лайков

Проект доступен по адресу http://konstantin05.ddns.net/

Админка http://konstantin05.ddns.net/admin

Логин: admin

Пароль: admin

## Пререквизиты

Docker

## Стек

DRF

PostgreSQL

Djoser

Gunicorn

Nginx

## Инструкции по запуску

git clone git@github.com:Konstantin8891/ItFox.git

cd backend

nano .env

DB_ENGINE=django.db.backends.postgresql

DB_NAME=postgres 

POSTGRES_USER=postgres 

POSTGRES_PASSWORD=postgres 

DB_HOST=db 

DB_PORT=5432

SECRET_KEY=django-insecure-pfu%+j%j-x!h*4q-clk&it*z@a*)km6#wwpe^$7rqf@cx8ewg%

ALGORITHM=HS256

cd ..

cd Infra_itfox

docker-compose up --build -d

docker-compose exec backend python manage.py collectstatic

docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

## Запросы к API

### Получение токена

POST http://konstantin05.ddns.net/auth/jwt/create

Body:

{

    "username": "admin",
    
    "password": "admin"
    
}

### Постим новость

 Требуется авторизация

POST 
