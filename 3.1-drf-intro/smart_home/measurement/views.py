"""
Виды представлений для работы с датчиками и измерениями.
Эти классы определяют логику обработки HTTP-запросов для различных операций.
"""
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from django.http import HttpResponse

@api_view(["GET"])
def api_root(request):
    """
    Корневой эндпоинт API.
    Возвращает информацию о доступных эндпоинтах.
    """
    return Response(
        {
            "message": "Welcome to Smart Home API!",
            "endpoints": {
                "sensors": {
                    "list": "/api/sensors/",
                    "detail": "/api/sensors/<int:pk>/",
                    "create": "/api/sensors/",
                    "update": "/api/sensors/<int:pk>/",
                    "delete": "/api/sensors/<int:pk>/",
                },
                "measurements": {
                    "list": "/api/measurements/",
                    "create": "/api/measurements/",
                    "view-image": "/api/measurements/<int:pk>/image/",
                },
            },
        }
    )

class SensorListCreateAPIView(generics.ListCreateAPIView):
    """
    Представление для работы со списком датчиков.
    Обеспечивает CRUD-операции над списком датчиков.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Представление для работы с отдельным датчиком.
    Обеспечивает чтение, обновление и удаление данных о конкретном датчике.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementListCreateAPIView(generics.ListCreateAPIView):
    """
    Представление для работы со списком измерений.
    Обеспечивает CRUD-операции над списком измерений.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Представление для работы с отдельным измерением.
    Обеспечивает чтение, обновление и удаление данных о конкретном измерении.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementImageView(generics.RetrieveAPIView):
    """
    Представление для просмотра изображения измерения.
    Возвращает изображение соответствующего измерения или сообщение об ошибке.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get(self, request, pk):
        measurement = Measurement.objects.get(pk=pk)

        if measurement.image:
            response = HttpResponse(content_type="image/jpeg")
            response["Content-Disposition"] = (
                f'inline; filename="measurement_{pk}.jpg"'
            )
            response.write(measurement.image.open().read())
            return response

        else:
            return Response(
                {"message": "Изображение отсутствует"}, status=status.HTTP_200_OK
            )