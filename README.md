Cоздать и активировать виртуальное окружение:

python -m venv venv

source venv/bin/activate

Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip

pip install -r requirements.txt

Выполнить миграции:

python manage.py makemigrations

python manage.py migrate

Запустить проект:

python3 manage.py runserver