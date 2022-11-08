# Пульт охраны банка

Сайт пульта охраны виртуального банка. 
- Отображает активные карты доступа. 
- По каждому посетителю выводит даты, время, продолжительность посещения.
- Список пользователей в хранилище. 

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте файл .env с переменными окружения:
```
ENGINE=[драйвер базы данных]
HOST=[адрес сервера]
PORT=[порт]
NAME=[название базы данных]
USER=[логин]
PASSWORD=[пароль]
SECRET_KEY=[секретный ключ]
```
Сайт запускается коммандой:
```
python3 manage.py runserver
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).