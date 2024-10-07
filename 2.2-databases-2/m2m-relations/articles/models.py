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
    # Переопределение метода __str__ для отображения имени тега в административном интерфейсе
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

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
    image = models.ImageField(upload_to='article_images/',null=True, blank=True, verbose_name="Изображение")

    # Связь ManyToMany с моделью Tag через промежуточную модель Scope
    tags = models.ManyToManyField(Tag, through="Scope", related_name='tag')


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
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Scope(models.Model):
    """
    Промежуточная модель для связи между статьями и тегами.

    Attributes:
    article (ForeignKey): Связь с моделью Article
    tag (ForeignKey): Связь с моделью Tag
    is_main (BooleanField): Флаг основного тега
    """

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    # Связь с моделью Article
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')  # Связь с моделью Tag
    is_main = models.BooleanField(default=False, verbose_name="Основной тег")  # Флаг основного тега

    class Meta:
        unique_together = ('article', 'tag')  # Уникальность пары статья-тег

    def clean(self):
        if self.is_main:
            if Scope.objects.filter(article=self.article, is_main=True).exclude(pk=self.pk).exists():
                raise ValidationError('Можно указать только один основной раздел для статьи')

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"
        # Строковое представление объекта Scope