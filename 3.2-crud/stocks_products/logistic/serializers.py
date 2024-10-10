""" Сериализаторы. """
from rest_framework import serializers
from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    Этот сериализатор используется для преобразования объектов Product в JSON и обратно.
    Он включает поля id, title и description.
    """
    class Meta:
        """
        Метакласс - настройка для конфигурации сериализатора.
        """
        model = Product
        fields = ('id', 'title', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели StockProduct.
    Этот сериализатор используется для представления позиций продуктов на складе.
    Он включает информацию о продукте, количестве и цене.
    """
    product = ProductSerializer()
    class Meta:
        """
        Метакласс для конфигурации сериализатора.
        """
        model = StockProduct
        fields = ('product', 'quantity', 'price')


class StockSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Stock.
    Этот сериализатор используется для преобразования объектов Stock в JSON и обратно.
    Он включает поля id и адрес склада.
    """
    positions = ProductPositionSerializer(many=True)

    class Meta:
        """
        Метакласс для конфигурации сериализатора.
        """
        model = Stock
        fields = ('id', 'address', 'positions')

    def create(self, validated_data):
        """
        Метод создания объекта Stock.
        Attributes:
        validated_data: Валидированные данные из запроса
        positions: Позиции продуктов
        product_data: Данные о продукте
        product: Продукт
        stock: Объект Stock
        StockProduct: Объект StockProduct
        Return: созданный объект Stock
        """
        # Достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # Создаем объект Stock по его параметрам
        stock = super().create(validated_data)
        # Добавляем связанные данные
        for position in positions:
            product_data = position.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            StockProduct.objects.create(stock=stock, product=product, **position)
        # Сохраняем объект Stock
        return stock

    def update(self, instance, validated_data):
        """
        Метод обновления объекта Stock.
        Attributes:
        instance: Существующий объект Stock
        validated_data: Валидированные данные из запроса
        positions: Позиции продуктов
        product_data: Данные о продукте
        product: Продукт
        stock: Объект Stock
        StockProduct: Объект StockProduct
        Return: Обновленный объект Stock
        """
        # Достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # Обновляем основную информацию по складу (по установленным параметрам)
        stock = super().update(instance, validated_data)
        # Обновляем связанные таблицы StockProduct с помощью списка positions
        for position in positions:
            product_data = position.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            StockProduct.objects.update_or_create(  # (8) изменение на update_or_create
                stock=stock,
                product=product,
                defaults=position
            )
        # Сохраняем изменения в объекте Stock
        return stock