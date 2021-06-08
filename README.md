### Требования
python >= 3.8

### Разработка
Чтобы запустить дев. сервер выполните следующие команды в терминале из папки `backend`:

1) `pip install -r requirements.txt`
2) `python manage.py migrate --run-syncdb`
3) `python manage.py runserver 8000 --settings=config.settings.development`

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