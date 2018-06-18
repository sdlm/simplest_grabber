# Задача пакета
Получить данные из произвольного исотчника.

```
path/url/credentials -> Grabber -> dict/list
```

# Пример использования
```
grabber = RSSGrabber(url=SOME_RSS_URL)
raw_data = grabber.load_data()
```

# Запуск тестов
```
python -m unittest grabber/tests/*
```

# Установка
```
pip install .
```