# UTF Tech Foods API

REST API для получения меню ресторана с категориями блюд и опубликованными товарами.

## Описание

API возвращает список категорий меню вместе с основными и дополнительными блюдами.
В выборку блюд попадают только те, которые являются опубликованными.
Дополнительные блюда также фильтруются по статусу публикации.

## Важно

В ТЗ не сказано про `internal_code=null`, включать ли его в выборку в `additional`.

Для `additional` в выборке блюд исключены все, что имеют `internal_code=null`, так как по `null` не получится связать связать его с конкретным `Food`.

По идее, нужно исключать все `Food`, так как единствееный уникальный индетификатор в ответе - это `internal_code`, если он будет `null`, то клиент потом не сможет передать информацию о конкретном `Food` на сервер


## Возможные улучшения

Добавить составной индекс по полям `Food.category_id` и `Food.is_pulished`, что позволило бы СУБД производить поиск за логарифмическое время, а не линейное.
Это ускорит поиск `FoodCategory`, где есть хотя бы один опубликованный `Food`
```sql
SELECT ...
FROM FoodCategory as food_category
WHERE EXISTS( SELECT 1 FROM Food as food WHERE food.category_id = food_category.id AND food.is_pulished)
...
```

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
