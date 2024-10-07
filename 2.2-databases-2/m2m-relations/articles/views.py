"""Модуль, содержащий представления для статей."""

from django.shortcuts import render
from .models import Article
from datetime import datetime

def articles_list(request):
    """
    Функция для вывода списка статей с оптимизированным запросом к базе данных.
    
    :param request: HTTP-запрос
    :return: Отрендерен шаблон с оптимизированным списком статей
    """
    
    # Определяем шаблон для отображения списка статей
    template = "articles/news.html"
    
    # Получаем все статьи, отсортированные по дате публикации
    # Используем prefetch_related для оптимизации запроса к базе данных
    object_list = Article.objects.all().order_by("-published_at").prefetch_related('scopes')
    
    print("Запрос к базе данных:", object_list.query)

    # Получаем основные теги для каждой статьи
    main_tags = []
    for article in object_list:
        scopes = article.scopes.all()
        for scope in scopes:
            if scope.is_main:
                main_tags.append(scope.tag)
                break

    # Формируем контекст для шаблона
    context = {
        "articles": object_list,
        "main_tags": main_tags,
    }

    # Проверка значений полей статьи
    for article in object_list:
        print(f"Заголовок: {article.title}")
        print(f"Текст: {article.text[:50]}...")  # Вывод первых 50 символов текста
        print(f"Изображение: {article.image}")

    print("Основные теги:", context["main_tags"])

    # Проверяем наличие основных тегов и статей
    if not context["main_tags"]:
        print("Основные теги не найдены")
    if not context["articles"]:
        print("Статьи не найдены")

    # Проверяем, что переменные передаются в шаблон правильно
    if "articles" in context and "main_tags" in context:
        print("Переменные передаются в шаблон правильно")
    else:
        print("Переменные не передаются в шаблон")

    # Возвращаем отрендеренный шаблон с контекстом
    return render(request, template, context)

# Метка времени последнего изменения
last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Последнее изменение: {last_modified}")