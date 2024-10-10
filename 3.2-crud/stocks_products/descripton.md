# Учебный проект (Продукты и склады - CRUD в DRF)

## Реализована связь моделей, представлений и сериализаторов в проекте

### Модели (сделано документирование)

В модели StockProduct связь один-ко-многим с моделью Product,
что позволяет связать каждый продукт со складом.

[models.py](/logistic/models.py)

### Представления (доработано)
В StockViewSet реализованы CRUD-операции для модели Stock.
В представлении StockViewSet мы используем StockSerializer для преобразования объектов Stock в JSON и обратно.
Этот сериализатор включает поля id, address и positions.
Поле positions сериализуется с помощью ProductPositionSerializer,
который включает информацию о продукте, количестве и цене.
Подключены фильтры и пагинацию.

[views.py](/logistic/views.py)

### Сериализаторы (доработано)
В ProductViewSet используется ProductSerializer, который сериализует поля id,
title и description модели Product.

В StockViewSet используется StockSerializer, который сериализует поля id,
address и positions модели Stock.
Поле positions сериализуется с помощью ProductPositionSerializer,
который сериализует информацию о продукте, количестве и цене.

Методы create и update в StockSerializer корректно обрабатывают связанные данные для других таблиц, что позволяет создавать и обновлять объекты Stock вместе с их позициями продуктов.
Использованы методы get_or_create и в методе update использовано update_or_create вместо create, чтобы избежать удаления существующих позиций продуктов на складе.

[serializers.py](/logistic/serializers.py)

### Примеры запросов (В проекте задан по условиям реализации файл примеров)
Добавлена реализованная возможность поиска складов, в которых есть определённый продукт, по назваю продукта
```
# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?search=помид
Content-Type: application/json
```

В запросах могут добавляться строки /HTTP/1.1 - не является обязательным,не влияет на работу кода, это часть HTTP-протокола, и указывает на версию протокола, используемую для передачи данных.
В большинстве случаев, не указфвается, поскольку она добавляется автоматически при отправке запроса.

 Можнно создать свой комплект рабочих примеров-тестов для складов и продуктов
```python
# requests.http

# 1-М УКАЗЫВАЕТСЯ БАЗОВЫЙ АДРЕС СЕРВЕРА
@baseUrl = http://localhost:8000/api/v1

# Запрос для метода update
#В этом примере мы отправляем PATCH-запрос на URL /api/stocks/1/, где 1 - идентификатор склада, который мы хотим обновить. В теле запроса мы передаем JSON-данные, 
# которые содержат новую информацию о складе, включая адрес и позиции продуктов.
PATCH /api/stocks/1/
Content-Type: application/json

{
  "address": "Новый адрес склада",
  "positions": [
    {
      "product": {
        "title": "Товар 1",
        "description": "Новое описание товара 1"
      },
      "quantity": 15,
      "price": 150.0
    },
    {
      "product": {
        "title": "Товар 2",
        "description": "Новое описание товара 2"
      },
      "quantity": 25,
      "price": 250.0
    }
  ]
}

###

# Запрос на получение списка складов
GET /stocks/ 
Content-Type: application/json

###

# Запрос на получение информации о конкретном складе
GET /stocks/1/ 
Content-Type: application/json

###

# Запрос на создание склада
POST /stocks/ 
Content-Type: application/json

{
  "address": "Москва, ул. Ленина, д. 1",
  "positions": [
    {
      "product": {
        "title": "Товар 1",
        "description": "Описание товара 1"
      },
      "quantity": 10,
      "price": 100.0
    },
    {
      "product": {
        "title": "Товар 2",
        "description": "Описание товара 2"
      },
      "quantity": 20,
      "price": 200.0
    }
  ]
}

####

#  Запрос на обновление склада с позициями продуктов
PUT /stocks/1/ 
Content-Type: application/json

{
  "address": "Москва, ул. Ленина, д. 1",
  "positions": [
    {
      "product": {
        "title": "Товар 1",
        "description": "Новое описание товара 1"
      },
      "quantity": 15,
      "price": 150.0
    },
    {
      "product": {
        "title": "Товар 2",
        "description": "Новое описание товара 2"
      },
      "quantity": 25,
      "price": 250.0
    }
  ]
}

### 

# Запрос на удаление склада
DELETE /stocks/1/ 
Content-Type: application/json

###

# PUT-запрос обычно используется для обновления существующей записи, а POST-запрос - для создания новой записи.
# В данном случае, PUT-запрос используется для обновления существующего склада с идентификатором 1, 
# а POST-запрос используется для создания нового склада.

###

# Запросы для продуктов
# Обновление продукта
PUT /api/products/1/ 
Content-Type: application/json

{
    "title": "Новое название продукта",
    "description": "Новое описание продукта"
}

###

# Создание продукта
POST /api/products/ 
Content-Type: application/json

{
    "title": "Новый продукт",
    "description": "Описание нового продукта"
}

###

# Удаление продукта
DELETE /api/products/1/ 
Content-Type: application/json

###

# Получение списка продуктов
GET /api/products/ 
Content-Type: application/json

###

# Получение информации о конкретном продукте
GET /api/products/1/ 
Content-Type: application/json

###

# Запросы для позиций продуктов на складе
# Обновление позиции продукта на складе
PUT /api/stocks/1/positions/1/ 
Content-Type: application/json

{
    "product": {
        "title": "Обновленный продукт",
        "description": "Обновленное описание продукта"
    },
    "quantity": 20,
    "price": 200.0
}

###

# Создание позиции продукта на складе
POST /api/stocks/1/positions/ 
Content-Type: application/json

{
    "product": {
        "title": "Новый продукт",
        "description": "Описание нового продукта"
    },
    "quantity": 10,
    "price": 100.0
}

###

# Удаление позиции продукта на складе
DELETE /api/stocks/1/positions/1/ 
Content-Type: application/json

###

# Получение списка позиций продуктов на складе
GET /api/stocks/1/positions/ 
Content-Type: application/json

###

# Получение информации о конкретной позиции продукта на складе
GET /api/stocks/1/positions/1/ 
Content-Type: application/json

###


# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?products=7
Content-Type: application/json

###

GET {{baseUrl}}/stocks/?search=Помидор
Content-Type: application/json
```

#### Для тестирования запросов необходимо сначала создать тестовую информацию в БД:
1. Через административную панель
последовательно: Продукты, Склады (Товарный объект), добавить Товары на складе (Стоковые товары)
2. Тоже Через API
путем запросов (см. выше)
3. Через интерактивный терминал
```bash
# Переход в интерактивный режим
python manage.py shell
# Запрос на список продуктов из БД
from logistic.models import Product
products = Product.objects.all()
print(products)
# Создание нового продукта
from logistic.models import Product
product = Product.objects.create(title='Новый продукт', description='Описание нового продукта')
print(product)
# Создание нового склада
from logistic.models import Stock
stock = Stock.objects.create(address='Москва, ул. Ленина, д. 1')
print(stock)
# Добавление продукта на склад
from logistic.models import StockProduct
stock_product = StockProduct.objects.create(stock=stock, product=product, quantity=10, price=100.0)
print(stock_product)
```
