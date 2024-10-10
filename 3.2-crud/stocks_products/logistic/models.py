""" Модели. """
from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    """
    Модель продуктов
    Attributes:
    title (CharField): Название продукта (уникальное).
    description (TextField): Описание продукта (необязательно).
    """
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)

class Stock(models.Model):
    """
    Модель склада.
    Attributes:
    address (CharField): Адрес склада (уникальный).
    products (ManyToManyField): Связь с продуктами через промежуточную таблицу StockProduct.
    """
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )

class StockProduct(models.Model):
    """
    Промежуточная модель для связи Stock и Product.
    Attributes:
    stock (ForeignKey): Связь с моделью Stock.
    product (ForeignKey): Связь с моделью Product.
    quantity (PositiveIntegerField): Количество продукта на складе.
    price (DecimalField): Цена хранения продукта на складе.
    """
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',  
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',   
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )