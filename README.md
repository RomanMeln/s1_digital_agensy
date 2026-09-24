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

---

## Запуск в Docker (Рекомендуемый)

Проект полностью докеризирован для быстрой и изолированной разработки.

### Быстрый старт:
1. Убедитесь, что у вас запущен **Docker Desktop**.
2. Создайте файл `.env` (если его еще нет).
3. В терминале в корне проекта выполните команду:
   ```bash
   docker compose up --build
   ```
   После сборки сайт будет доступен по адресу: `http://127.0.0`

### ⚠️ Важное примечание для Windows:
Контейнеры Docker работают на базе ОС Linux, которая использует Unix-формат переноса строк (**LF**).
Windows по умолчанию использует формат **CRLF**. 

Если при запуске контейнера вы получаете ошибку `standard_init_linux.go... no such file or directory`, это означает,
что Git или ваш редактор кода (PyCharm/VS Code) изменили окончания строк в конфигурационных файлах.

**Возможное исправление:**
1. Перед клонированием репозитория на Windows выполните команду:
   ```bash
   git config --global core.autocrlf input
   ```
2. Если проект уже склонирован, откройте проект в PyCharm, в правом нижнем углу окна редактора найдите
переключатель `CRLF` и переведите его в режим `LF` для файлов `Dockerfile` и `docker-compose.yml`.