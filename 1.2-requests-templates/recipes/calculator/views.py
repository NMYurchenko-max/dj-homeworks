from django.shortcuts import render  # Импортируем функцию render для рендеринга шаблонов

# Словарь с рецептами
DATA = {
    'omlet': {  # Рецепт омлета
        'яйца, шт': 2,  
        'молоко, л': 0.1,  
        'соль, ч.л.': 0.5,  
    },
    'pasta': {  # Рецепт пасты
        'макароны, г': 0.3,  
        'сыр, г': 0.05,  
    },
    'buter': {  # Рецепт бутерброда
        'хлеб, ломтик': 1,  
        'колбаса, ломтик': 1,  
        'сыр, ломтик': 1,  
        'помидор, ломтик': 1,  
    },
}

def all_recipes_view(request, recipe_name=None):  
    # Определяем функцию представления
    if recipe_name is None:  
    # Если имя рецепта не передано
        # Создаем контекст для шаблона, содержащий список всех рецептов
        context = {'recipes': list(DATA.keys())}  
        # Получаем список всех рецептов
    elif recipe_name in DATA:  
        # Если имя рецепта есть в словаре DATA
        # Создаем контекст для шаблона
        context = {
            'recipe': DATA[recipe_name],  # Получаем рецепт по имени
            'servings': request.GET.get('servings'),  # Получаем количество порций из GET-запроса
            'recipe_name': recipe_name  # Передаем название рецепта в контекст
        }
        # Обработка количества порций
        if context['servings']:  # Если количество порций передано
            try:
                # Преобразуем servings из строки в целое число
                servings = int(context['servings'])
                # Умножаем количество ингредиентов на количество порций
                for ingredient in context['recipe']:  
                    # Перебираем ингредиенты
                    context['recipe'][ingredient] = DATA[recipe_name][ingredient] * servings
            except ValueError:  # Обрабатываем ошибку при преобразовании servings в число
                pass  # Игнорируем ошибку, если не удалось преобразовать
    else:  # Если рецепт не найден
        context = {'error_message': f'Рецепт "{recipe_name}" не найден'}  
        # Сообщение об ошибке
    return render(request, 'calculator/index.html', context=context)  
    # Рендерим шаблон с контекстом
    