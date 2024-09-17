from django.contrib import admin  
# Импортируем админку Django
from django.urls import path, include  
# Импортируем функции path и include

urlpatterns = [
    path('admin/', admin.site.urls),  
    # Путь для админки
    path('recipes/', include('calculator.urls')),  
    # Подключаем URL-ы приложения calculator
]