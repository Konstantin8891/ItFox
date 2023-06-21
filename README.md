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

### Получаем список всех новостей

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

### Получаем одну новость

GET http://konstantin05.ddns.net/news/1/

Ответ:

{

    "id": 1,
    
    "title": "1 новость",
    
    "text": "Текст",
    
    "author": 1,
    
    "likes": 0,
    
    "comments": []
    
}

### Обновляем новость

Требуется авторизация по токену. Правами для изменения новости обладает только администратор и автор.

PUT http://konstantin05.ddns.net/news/1/

Body:

{

    "title": "1 новость",
    
    "text": "put"
    
}

Ответ:

{

    "id": 1,
    
    "title": "1 новость",
    
    "text": "put",
    
    "author": 1,
    
    "likes": 0
    
}

### Удаляем новость

Требуется авторизация по токену. Правами для удаления новости обладает только администратор и автор.

DELETE http://konstantin05.ddns.net/news/1/

### Оставляем комментарий

Требуется авторизация по токену

POST http://konstantin05.ddns.net/news/2/comments/

Body:

{

    "text": "1 комментарий"
    
}

Ответ:

{

    "text": "1 комментарий",
    
    "author_id": 1
    
}

### Получение всех комментариев 

Поддерживается пагинация

GET http://konstantin05.ddns.net/news/2/comments/

{

    "count": 1,
    
    "next": null,
    
    "previous": null,
    
    "results": [
    
        {
        
            "id": 1,
            
            "text": "1 комментарий",
            
            "author_id": 1
            
        }
        
    ]
    
}

### Удаление комментария

Требуется авторизация по токену. Правами для удаления комментария обладает только администратор и автор.

DELETE http://konstantin05.ddns.net/news/2/comments/1/

### Поставить лайк новости

GET http://konstantin05.ddns.net/news/2/like/

Ответ:

{

    "id": 2,
    
    "title": "Первая новость",
    
    "text": "Текст",
    
    "author": 1,
    
    "likes": 1
    
}
