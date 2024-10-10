""" Вьюшки. """
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    pagination_class = StandardResultsSetPagination
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    """
    Вьюшка для модели Product.
    Поддерживает фильтрацию.
    Поддерживает поиск по названию и описанию.
    """
    queryset = Product.objects.all()     # Все продукты
    serializer_class = ProductSerializer     # Используемый сериализатор
    filter_backends = (filters.SearchFilter,)    # Поддержка фильтрации
    search_fields = ('id', 'title', 'description')    # Поиск по названию и описанию, id
    pagination_class = StandardResultsSetPagination     # Поддержка пагинации


class StockViewSet(viewsets.ModelViewSet):
    """
    Вьюшка для модели Stock.
    Поддерживает фильтрацию.
    Поддерживает поиск по адресу.
    Поддерживает фильтрацию по id и адресу.
    """
    queryset = Stock.objects.all()     # Все склады
    serializer_class = StockSerializer     # Используемый сериализатор
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)    # (9) изменение на SearchFilter и DjangoFilterBackend
    search_fields = ('address',)    # Поиск по адресу
    filterset_fields = ['id', 'address']  # пример на основе наличия id и адреса
    pagination_class = StandardResultsSetPagination     # Поддержка пагинации
