# Энциклопедия

Скрипт ```site_generator.py``` генерирует страницы HTML из markdown файлов и  собирает из низ статический сайт. Пример сайта доступен на GitHub Pages по следующей ссылке: [пример сайта](https://igorzakhar.github.io/19_site_generator/)  

# Установка

Программа требует для своей работы установленного интерпретатора Python версии 3.5.  
Так же в программе используются сторонние библиотеки:
- [jinja2](http://jinja.pocoo.org/docs/2.10/)
- [markdown](https://python-markdown.github.io/)

Используйте команду pip для установки библиотек из файла зависимостей (или pip3 если есть конфликт с предустановленным Python 2):
```
$ pip install -r requirements.txt # В качестве альтернативы используйте pip3
```
Рекомендуется устанавливать зависимости в виртуальном окружении, используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) или [venv](https://docs.python.org/3/library/venv.html). 

# Использование

Пример запуска в Linux, Python 3.5.2:
```
$ python3 site_generator.py
```
В результате генерируется HTML страницы и размещаются в директории ```site```. Структура сайта организована на основе конфигурационного файла ```config.json``` 

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
