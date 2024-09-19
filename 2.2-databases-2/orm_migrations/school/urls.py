from django.urls import path

from school.views import students_list

# Список URL-паттернов для маршрутизации запросов внутри приложения 'school'
urlpatterns = [
    # URL '/students/' будет сопоставляться с представлением students_list
    path("students/", students_list, name="students"),
    # Тестовые ссылки, показвают:
    path("test_students/", students_list, name="test_students"),
    # Обычный список студентов с преподаателями
    path(
        "test_student_without_teacher/",
        lambda request: students_list(request),
        name="test_student_without_teacher",
    ),
    # Студенты без преподавателей
    path(
        "test_empty_class/",
        lambda request: students_list(request),
        name="test_empty_class",
    ),
    # Пустой класс
    path(
        "test_debug_mode/",
        lambda request: students_list(request),
        name="test_debug_mode",
    ),
    # Отладочную информацию
]
