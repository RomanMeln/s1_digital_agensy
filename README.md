Заполнить .env на примере .env.examle  
SECRET_KEY='КЛЮЧ'  
DEBUG=True #или False  

В проекте есть тестовые данные.  
Чтобы заполнить тестовые данные для базы данных,  
введите команды:
```bash
python manage.py loaddata projectapp/fixtures/projects.json
python manage.py loaddata blogapp/fixtures/categories.json
python manage.py loaddata blogapp/fixtures/posts.json
```
или 1 команду:
```bash
python manage.py loaddata projectapp/fixtures/projects.json blogapp/fixtures/categories.json blogapp/fixtures/posts.json
```
