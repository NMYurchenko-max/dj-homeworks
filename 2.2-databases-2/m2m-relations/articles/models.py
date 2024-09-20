""" Модуль, содержащий модели для представления статей и связей между ними. """

from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    """
    Модель для представления тегов.

    Attributes:
    name (CharField): Имя тега
    """

    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Модель для представления статей.

    Attributes:
    title (CharField): Заголовок статьи
    text (TextField): Текст статьи
    published_at (DateTimeField): Дата публикации
    image (ImageField): Изображение статьи
    scopes (ManyToManyField): Связь с тегами через Scope
    """

    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")
    scopes = models.ManyToManyField(Tag, through="Scope")

    def clean(self):
        """
        Проверяет, не существует ли статьи с таким названием.

        Raises:
        ValidationError: Если статья с таким названием уже существует
        """
        if self.pk is None:  # Проверяем только при создании новой статьи
            if Article.objects.filter(title=self.title).exists():
                raise ValidationError("Статья с таким названием уже существует")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
