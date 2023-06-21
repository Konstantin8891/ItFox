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

Требуется авторизация по токену Bearer {token}

POST http://konstantin05.ddns.net/news/

Body:

{

    "title": "Вторая новость",
    
    "text": "Текст"
    
}

Ответ:

{

    "id": 3,
    
    "title": "Вторая новость",
    
    "text": "Текст",
    
    "author": 1,
    
    "likes": 0
    
}

GET http://konstantin05.ddns.net/news/

Ответ поддерживает пагинацию (6 ответов на страницу):

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "1 новость",
            "text": "Текст",
            "author": 1,
            "likes": 0,
            "comments": []
        },
        {
            "id": 2,
            "title": "Первая новость",
            "text": "Текст",
            "author": 1,
            "likes": 0,
            "comments": []
        },
        {
            "id": 3,
            "title": "Вторая новость",
            "text": "Текст",
            "author": 1,
            "likes": 0,
            "comments": []
        }
    ]
}
