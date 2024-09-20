""" Модуль, содержащий представления для статей. """

from django.shortcuts import render
from .models import Article


def articles_list(request):
    """
    Функция для вывода списка статей с оптимизированным запросом к базе данных.

    :param request: HTTP-запрос
    :return: Отрендерен шаблон с оптимизированным списком статей
    """
    template = "articles/news.html"

    # Получаем все статьи, отсортированные по дате публикации
    articles = Article.objects.all().order_by("-published_at")

    context = {
        "object_list": articles
        # Передаем список статей в контекст
    }

    return render(request, template, context)
