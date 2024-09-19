from django.conf import settings

# from django.views.generic import ListView
from django.shortcuts import render
import logging

# Импорт моделей Student и Teacher из текущего приложения
from .models import Student, Teacher

# Создание логгера для отслеживания выполнения запросов
logger = logging.getLogger(__name__)


def students_list(request):
    # Логирование начала обработки запроса
    logger.info("Starting students_list request")

    # Определение имени шаблона для рендеринга
    template = "school/students_list.html"

    # Получение всех студентов с предварительной загрузкой связанных преподавателей,
    # добавлен prefetch_related для оптимизации запросов к базе данных
    students = Student.objects.prefetch_related("teachers").all
    # Получение всех преподавателей

    # Создание словаря контекста для передачи в шаблон
    context = {
        "students": students,
        "debug": settings.DEBUG,
        # Флаг отладки
    }

    # Рендеринг шаблона с передачей запроса, шаблона и контекста
    return render(request, template, context)
