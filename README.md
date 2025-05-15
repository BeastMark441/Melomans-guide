# Справочник меломана

Веб-приложение для любителей музыки, позволяющее просматривать информацию об исполнителях, альбомах, треках, а также делиться отзывами и создавать личные коллекции.

## Функциональность

- Просмотр списка исполнителей и их альбомов
- Просмотр информации об альбомах и треках
- Чтение новостей музыкальной индустрии
- Возможность оставлять отзывы об альбомах
- Создание личной коллекции альбомов
- Регистрация и авторизация пользователей

## Технологии

- Python 3.13+
- Django 5.2+
- Bootstrap 5
- SQLite

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/BeastMark441/Melomans-guide.git
cd mymusic
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Тестовые пользователи

В системе уже созданы тестовые пользователи:

1. Администратор:
   - Логин: `admin`
   - Пароль: `admin`

2. Тестовый пользователь:
   - Логин: `testuser`
   - Пароль: `testuser`

## Использование

1. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`
2. Зарегистрируйтесь или войдите в систему
3. Начните исследовать музыкальный каталог!

## Лицензия

MIT License

Copyright (c) 2025 BeastMark

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
