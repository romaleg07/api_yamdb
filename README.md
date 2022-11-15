# Yamdb API
Yamdb это RESTful API для вымышленного сайта ценителей различных произведений культуры.
Реализованы: регистрация и аутентификация по JWT токенам, добавление произведений различных категорий и жанров, отзывы и комментарии, модерация. Все это упаковано в контейнеры Docker`а для быстрого развертывания проекта.

Произведения делятся на следующие категории: «Книги», «Фильмы», «Музыка». Администратор может расширить список категорий, а также удалять произведения, категории и жанры, назначать роли пользователям.
Зарегистрированные пользователи могут оставлять к произведениям текстовые отзывы и ставить оценку в диапазоне от одного до десяти произведениям, комментировать отзывы. Также они могут редактировать и удалять свои отзывы и комментарии, свои оценки произведений.

Yamdb был написан мной в рамках учебного проекта, целью которого было изучение Django REST Framework и механизмов аутентификации по токенам. База данных на основе PosgreSQL и Django ORM.

**Технологии:** Django, Django REST Framework, JWT, Docker, PosgreSQL, Docker-compose, Nginx, Gunicorn

## Технологии:
- [Django](https://www.djangoproject.com/) - Мощный framework для Python!
- [Django REST Framework](https://www.django-rest-framework.org) - мощный и гибкий инструмент для создания Web APIs
- [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - JSON-токен для аутентификации.
- [Docker](https://www.docker.com) - интструмент для автоматизации развертывания приложений
- [Docker-compose](https://docs.docker.com/compose/) - приложение для развертывания нескольких контейнеров
- [PosgreSQL](https://www.postgresql.org) - база данных
- [Nginx](https://nginx.org/) - HTTP-сервер для статических данных
- [Gunicorn](https://gunicorn.org) - HTTP-сервер для динамических данных Django

## Установка

### Версии стека
Подробнее в requirements.txt
```
Python 3.7.9
Django 2.2.16
Django REST Framework 3.12.4
PyJWT 2.1.0
Requests 2.26.0
``` 

### Деплой
Установить и настроить докер.

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/romaleg07/api_yamdb.git
``` 
Создать файл с перменными
1) В папке "infra" создайте файл с названием ".env" без расширения
2) в файл .env добавьте перменные со значениями:
``` 
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<your_password>
DB_HOST=db
DB_PORT=5432
```
Забилдить и поднять проект:
```
$ docker-compose up -d --build 
``` 
После развертывания проекта нужно выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Создать суперюзера:
```
$ docker-compose exec web python manage.py createsuperuser
```
Собрать статику для сайта:
```
$ docker-compose exec web python manage.py collectstatic --no-input
```
Применить фикстуры:
```
docker-compose exec web python manage.py loaddata fixtures.json
```

## Проект развернут!
