# MasterPol

Графическое приложение на PyQt6 для работы с базой данных MySQL.

## Подготовка проекта

1. **Клонируйте репозиторий и перейдите в папку проекта:**

   ```sh
   git clone <адрес-репозитория>
   cd master_pol
   ```

2. **Создайте и активируйте виртуальное окружение:**

   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/MacOS
   ```

3. **Установите зависимости:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Создайте базу данных и выполните SQL-скрипт:**

   - Запустите MySQL и выполните скрипт `app/database/script.sql` для создания необходимых таблиц и данных:

   ```sh
   mysql -u <user> -p <db_name> < app/database/script.sql
   ```

   - Замените `<user>` и `<db_name>` на свои значения.

5. **Проверьте параметры подключения к базе данных:**
   - Откройте файл `app/database/db.py` и убедитесь, что значения для подключения (host, user, password, database) указаны верно.

## Запуск приложения

```sh
python app/main.py
```

## Структура проекта

- `app/main.py` — точка входа, запуск приложения
- `app/components/` — компоненты интерфейса
- `app/database/` — работа с БД, скрипты и настройки
- `app/pages/` — страницы приложения
- `app/res/` — ресурсы (цвета, шрифты)

---
