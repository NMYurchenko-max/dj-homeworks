"""
Этот файл содержит функциональные представления для работы с API.
"""

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
                "sensors": "/api/sensors/",
                "measurements": "/api/measurements/",
            },
        }
    )


@api_view(["GET", "POST"])
def sensor_list(request):
    """
    Эндпоинт для работы со списком датчиков.

    GET: Возвращает список всех датчиков или создает новый датчик.
    POST: Создает новый датчик.
    """
    if request.method == "GET":
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def sensor_detail(request, pk):
    """
    Эндпоинт для работы с отдельным датчиком.

    GET: Возвращает информацию о конкретном датчике.
    PUT: Обновляет информацию о конкретном датчике.
    DELETE: Удаляет конкретный датчик.
    """
    try:
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def measurement_list(request):
    """
    Эндпоинт для работы со списком измерений.

    GET: Возвращает список всех измерений или создает новое измерение.
    POST: Создает новое измерение.
    """
    if request.method == "GET":
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def view_measurement_image(request, pk):
    """
    Эндпоинт для просмотра изображения измерения.

    GET: Возвращает изображение конкретного измерения или информацию об отсутствии изображения.
    """
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
