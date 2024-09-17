from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone
import logging

logger = logging.getLogger(__name__)
# Логирование добавлено для контроля

def index(request):
    # Приводит пользователя на страницу каталога
    logger.debug("Вернуться в каталог")
    return redirect('catalog')


def show_catalog(request):
    # Отображает список телефонов с возможностью сортировки
    logger.debug("Отображение каталога")
    sort_option = request.GET.get('sort', 'name')
    if sort_option == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_option == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')

    return render(request, 'catalog.html', {'phones': phones})


def show_product(request, slug):
    # Отображает детали отдельного телефона по его слагу
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})