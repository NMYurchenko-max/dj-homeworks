"""
Этот файл содержит определения URL-путей для API приложения smart_home.
"""

# Импорт необходимых модулей из Django
from django.urls import path

# Импорт view-функций
from .views import (
    api_root,
    sensor_list,
    sensor_detail,
    measurement_list,
    view_measurement_image,
)

urlpatterns = [
    # URL-путь для корневой страницы API
    path("", api_root, name="api-root"),
    # URL-путь для получения списка датчиков и создания нового датчика
    path("sensors/", sensor_list, name="sensor-list-create"),
    # URL-путь для получения, обновления и удаления конкретного датчика
    path(
        "sensors/<int:pk>/", sensor_detail, name="sensor-retrieve-update-delete"
    ),
    # URL-путь для получения списка измерений и создания нового измерения
    path("measurements/", measurement_list, name="measurement-create"),
    # URL-путь для просмотра изображения измерения
    path(
        "measurements/<int:pk>/image/",
        view_measurement_image,
        name="view-measurement-image",
    ),
]

"""
http://127.0.0.1:8000/api/ для корневой страницы API
http://127.0.0.1:8000/api/sensors/ для работы с датчиками
http://127.0.0.1:8000/api/sensors/<id>/ для работы с отдельным датчиком
http://127.0.0.1:8000/api/measurements/ для работы с измерениями
http://127.0.0.1:8000/api/measurements/<id>/image/ для просмотра изображения измерения
"""
