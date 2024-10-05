"""
Сериализаторы для моделей Sensor и Measurement.
Эти классы отвечают за преобразование объектов Django в JSON и обратно.
"""
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Sensor, Measurement


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


class SensorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Sensor.
    Поля:
    id - идентификатор датчика
    name - название датчика
    description - описание датчика
    """
    measurements = serializers.SerializerMethodField()

    class Meta:
        # Модель, которую сериализуем
        model = Sensor

        # Все поля модели включены в сериализацию
        fields = ["id", "name", "description", "measurements"]

    def get_measurements(self, obj):
        # Возвращаем список измерений для данного датчика
        measurements = obj.measurements.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return serializer.data


class SensorListCreateView(ListCreateAPIView):
    """
    Представление для работы со списком датчиков.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельным датчиком.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    """
Вложенность сериализаторов:
В сериализаторе SensorSerializer есть поле measurements, 
которое представляет собой список измерений для данного датчика. 
Для сериализации этого списка используется сериализатор MeasurementSerializer.

В методе get_measurements сериализатора SensorSerializer используется сериализатор 
MeasurementSerializer для сериализации списка измерений. 
Это позволяет получить вложенную структуру данных, где каждый датчик содержит список своих измерений.

Например, если у вас есть датчик с идентификатором 1 и он имеет два измерения с идентификаторами 1 и 2, 
то сериализатор SensorSerializer вернет следующую структуру данных:

```json
{
  "id": 1,
  "name": "Датчик 1",
  "description": "Описание датчика 1",
  "measurements": [
    {
      "id": 1,
      "sensor": 1,
      "temperature": 20,
      "created_at": "2022-01-01T12:00:00",
      "image": null
    },
    {
      "id": 2,
      "sensor": 1,
      "temperature": 25,
      "created_at": "2022-01-02T12:00:00",
      "image": null
    }
  ]
}
```
    """