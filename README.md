# Сокращения URL-адресов
Этот скрипт на Python предназначен для сокращения URL-адресов и для подсчёта переходов по сокращённым ссылкам используя API bitly.com

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Для правильной работы программы необходимо настроить переменные окружения:
Создайте файл .env в корневой директории проекта и определите в нем переменную окружения.
```
BITLY_TOKEN=Ваш API токен
```
BITLY_TOKEN токен необходим для работы с API сервисом Bitly.\
Подробнее в документации https://dev.bitly.com/api-reference.
### Как пользоваться
Чтобы воспользоваться этим скриптом, выполните следующие шаги:

Запустите скрипт:
```
python main.py
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).