"""
URL конфигурация для API приложения Smart Home.
Этот файл определяет все маршруты API для работы с датчиками и измерениями.
"""
from django.urls import path
from .views import (
    api_root,
    SensorListCreateAPIView,
    SensorRetrieveUpdateAPIView,
    MeasurementListCreateAPIView,
    MeasurementRetrieveUpdateAPIView,
    MeasurementImageView,
)

urlpatterns = [
    # URL-путь для корневого эндпоинта API
    path('', api_root, name='api_root'),
    # URL-путь для получения списка датчиков и создания нового датчика
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor_list'),
    # URL-путь для получения, обновления и удаления отдельного датчика
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor_detail'),
    # URL-путь для получения списка измерений и создания нового измерения
    path('measurements/', MeasurementListCreateAPIView.as_view(), name='measurement_list'),
    # URL-путь для просмотра изображения измерения
    path('measurements/<int:pk>/image/', MeasurementImageView.as_view(), name='view_measurement_image'),
]

"""
Доступные эндпоинты для проверки:

Сенсоры

GET http://localhost:8000/api/sensors/ - список всех датчиков
POST http://localhost:8000/api/sensors/ - создание нового датчика
GET http://localhost:8000/api/sensors/<int:pk>/ - получение информации о конкретном датчике
PUT http://localhost:8000/api/sensors/<int:pk>/ - обновление информации о конкретном датчике
DELETE http://localhost:8000/api/sensors/<int:pk>/ - удаление конкретного датчика

Измерения

GET http://localhost:8000/api/measurements/ - список всех измерений
POST http://localhost:8000/api/measurements/ - создание нового измерения
GET http://localhost:8000/api/measurements/<int:pk>/image/ - просмотр изображения конкретного измерения

Корневой эндпоинт

GET http://localhost:8000/api/ - список всех доступных эндпоинтов
Вы можете использовать эти ссылки для проверки доступных эндпоинтов и их функциональности.

"""