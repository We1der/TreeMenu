# TreeMenu
### Данный проект является тестовым заданием. Выолнено древовидное меню с использованием django и стандартных библиотек python
Меню можно использовать с помощью templatetags: {% draw_menu 'menu_name' %}.
Оно хранится в БД (для задания используется станадартная SQLite)
Редактировать меню можно через админ зону

## Запуск проекта:
- Клонируйте репозиторий:
```
git@github.com:We1der/TreeMenu.git
```
- Установите и активируйте виртуальное окружение (venv)
- Установите пакеты и библиотеки из requirements.txt
```
pip install -r requirements.txt
``` 
- Запустите команду находясь в папке с файлом manage.py:
```
python3 manage.py runserver
```

### Author
Mikhail Frolov