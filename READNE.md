Для запуска проекта необходимо совершить следующее:

Создать и заполнить файл .env по шаблону .env.sample

Развернуть виртуальное окружение .venv

Установить зависимости с помощью pip install -r requirements.txt

Создать базу данных

Применить миграции с помощью python manage.py migrate

Запустить следующие команды (каждую в своём процессе)

redis-server
celery -A config worker -l info
celery -A config beat
python manage.py runserver

# Курсовая 8
# Для запуска:
Заполнить файл .env.sample, изменить его название на .env
ввести команду "docker compose up"
python manage.py runserver