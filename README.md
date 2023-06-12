# Генератор паролей ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
## О сервисе
##### Этот сервис генерации паролей создан в рамках учебного курса "Django 3 - Full Stack разработка веб сайтов на Python" с сайта https://beonmax.com
##### Год создания 2023
##### Автор: Репин Павел
## Условия для использования продукта
##### Python = 3.11
##### Django = 4.2.2
### Установка

- Установить PYTHON3 и PIP
- Установить virtualenv с помощью sudo pip
- Перейти в каталог проекта (создать, если он не существует)
- ``virtualenv -p python3 ``
- ``исходный файл / активировать ``
- ``установить Django с помощью pip``

### Запустить проект

- ``virtualenv -p python3``
- ``source env/bin/activate``
- ``python manage.py runserver host:port``(поместить хост в /etc/hosts, по умолчанию 127.0.0.1:8000)

### Тесты Django

- Создавать тесты в generator/tests.py файл
- ``python manage.py test polls``
