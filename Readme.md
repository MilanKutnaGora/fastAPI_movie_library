# Movie Library API

Это мини API для фильмотеки, написанный на Python с использованием FastAPI и SQLAlchemy. API позволяет управлять пользователями, фильмами и списками избранного.

## Функциональность

- **Пользователи**
  - Создание пользователей
  - Изменение данных пользователя
  - Удаление пользователя

- **Фильмы**
  - Добавление новых фильмов
  - Изменение данных о фильме
  - Удаление фильмов

- **Избранное**
  - Добавление фильмов в список избранного для пользователя
  - Удаление фильмов из списка избранного
  - Получение списка избранных фильмов для конкретного пользователя

## Установка

1. Клонируйте репозиторий:

   git clone <URL_вашего_репозитория>
   cd movie_library
   
2. Установите зависимости:
`pip install -r requirements.txt`

Запуск
Запустите сервер с помощью Uvicorn:
`uvicorn app.main:app --reload`