""" Модуль, содержащий URL-адреса для статей. """

from django.urls import path
from articles.views import articles_list

urlpatterns = [
    path("", articles_list, name="articles"),
    # URL-путь для просмотра списка статей
]
