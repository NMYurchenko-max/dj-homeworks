from django.db import models
from django.utils.text import slugify
from django.contrib import admin

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    # Автоматически генерируемое поле ID

    name = models.CharField(max_length=255)
    # Хранит имя телефона (до 255 символов)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Точное значение цены (до 10 цифр, 2 десятичных знака)

    image = models.URLField()
    # Изображение телефона хранится как URL (для экономии места и возможности использования CDN)

    release_date = models.DateField()
    # Дата выпуска телефона

    lte_exists = models.BooleanField(default=False)
    # Поле для хранения информации о поддержке LTE

    slug = models.SlugField(unique=True, blank=True)
    # Поле для хранения URL-слага (короткого читаемого URL-адреса)

    def save(self, *args, **kwargs):
        # Метод для автоматического создания слага при сохранении объекта
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        # Строковое представление объекта (используется в админ-панели)
        return self.name
