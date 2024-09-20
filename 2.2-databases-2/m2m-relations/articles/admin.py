""" Модуль, содержащий административное представление для статей. """

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    """
    Формсет для валидации связей Scope.

    Проверяет, что у статьи есть только один основной тег.
    """

    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data.get("is_main"):
                main_tag_count += 1
        if main_tag_count > 1:
            raise ValidationError("Только один тег может быть основным.")

        return super().clean()


class ScopeInline(admin.TabularInline):
    """
    Инлайн-форм для отображения связей Scope в административном интерфейсе.

    Attributes:
    model (Model): Модель Scope
    formset (BaseInlineFormSet): Формсет для валидации
    extra (int): Количество пустых форм для добавления новых связей
    """

    model = Scope
    formset = ScopeInlineFormset
    extra = 1
    # Добавляет одну пустую форму для нового тега


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Административное представление для модели Article.

    Attributes:
    inlines (list): Список инлайн-форм для отображения связей
    """

    inlines = [ScopeInline]
    # Использует ScopeInline для отображения связей


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Административное представление для модели Tag.
    """

    list_display = ("name",)
    search_fields = ("name",)
