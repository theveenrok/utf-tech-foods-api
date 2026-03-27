# UTF Tech Foods API

REST API для получения меню ресторана с категориями блюд и опубликованными товарами.

## 📋 Описание

API возвращает список категорий меню вместе с основными и дополнительными блюдами.
В выборку блюд попадают только те, которые являются опубликованными.
Дополнительные блюда также фильтруются по статусу публикации.

**Важно**
В ТЗ не сказано про `internal_code=null`, включать ли его в выборку в `additional`.

## Структура проекта

```
utf-tech-foods-api/
├── apps/
│   ├── shared/         # Общие инструменты
│   └── menu/           # Приложение меню
│       ├── models.py   # Модели Food, FoodCategory
│       ├── views.py    # API views
│       ├── serializers.py
│       └── tests.py    # Тесты
├── config/             # Настройки Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── pyproject.toml
└── README.md
```

## Авторы

- **Vlad Korneev** — [veenrok@veenrok.com](mailto:veenrok@veenrok.com)
