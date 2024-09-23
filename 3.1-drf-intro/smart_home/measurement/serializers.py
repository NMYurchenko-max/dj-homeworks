"""
Этот файл содержит сериализаторы для преобразования данных между Python-объектами и JSON.
"""

from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Sensor.

    Поля:
    id - идентификатор датчика
    name - название датчика
    description - описание датчика
    """

    class Meta:
        # Модель, которую сериализуем
        model = Sensor

        # Все поля модели включены в сериализацию
        fields = ["id", "name", "description"]


class MeasurementSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Measurement.

    Поля:
    id - идентификатор измерения
    sensor - связанный датчик
    temperature - измеренная температура
    created_at - дата и время измерения
    image - изображение измерения
    """

    class Meta:
        # Модель, которую сериализуем
        model = Measurement

        # Все поля модели включены в сериализацию
        fields = ["id", "sensor", "temperature", "created_at", "image"]
