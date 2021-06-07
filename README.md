### Разработка
Чтобы запустить дев. сервер выполните команду из папки backend:

`python manage.py runserver 8000 --settings=config.settings.development`

### Докер
1) Переименуйте файл `.env.example` в `.env`
2) Заполните переменные окружения в `.env` файле
3) Чтобы запустить приложение в докер выполните команду из корня папки:
`docker-compose up --build -d`
4) Чтобы запустить без докера выполните команду:
`python manage.py runserver 8000`
   
### Создание пользователя админа
Чтобы создать администратора в дев. режиме выполните команду:

`python manage.py createsuperuser --settings=config.settings.development`

Чтобы создать администратора в прод. режиме:

`python manage.py createsuperuser`

В стандартной базе `db.sqlite3` уже есть администратор и тестовые данные:

`Логин: admin`
`Пароль: admin`