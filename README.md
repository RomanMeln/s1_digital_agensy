Заполнить .env на примере .env.examle
SECRET_KEY='КЛЮЧ'
DEBUG=True #или False


Заполнить тестовые данные для базы данных:
python manage.py loaddata projectapp/fixtures/projects.json
python manage.py loaddata blogapp/fixtures/posts.json