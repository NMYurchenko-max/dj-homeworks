import pytest
from model_bakery import baker
from pytest_django.fixtures import client
from rest_framework.test import APIClient

from random import randint
from students.models import Course, Student


# Фикстура для создания экземпляра APIClient
@pytest.fixture
def client():
    return APIClient()


# Фабричная функция для создания объектов Student
@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# Фабричная функция для создания объектов Course
@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Тест получения одиночного курса
@pytest.mark.django_db
def test_get_courses(client, courses_factory):
    # Создаем 1000 курсов с помощью фикстуры courses_factory
    courses = courses_factory(_quantity=1000)

    # Отправляем GET-запрос для получения первого курса
    response = client.get(f"/api/v1/courses/{courses[0].id}/")

    assert response.status_code == 200
    assert response.json()["name"] == courses[0].name


# Тест получения списка курсов
@pytest.mark.django_db
def test_get_course_list(client, courses_factory):
    # Создаем 100 курсов с помощью фикстуры courses_factory
    courses = courses_factory(_quantity=100)

    # Отправляем GET-запрос для получения всех курсов
    response = client.get("/api/v1/courses/")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)


# Тест фильтрации курсов по ID
@pytest.mark.django_db
def test_filter_by_id(client, courses_factory):
    # Создаем 10 курсов с помощью фикстуры courses_factory
    courses = courses_factory(_quantity=10)

    # Выбираем случайный ID из созданных курсов
    random_id = [i.id for i in courses][randint(0, 9)]

    # Отправляем GET-запрос для фильтрации курсов по случайному ID
    response = client.get(f"/api/v1/courses/?id={random_id}")
    data = response.json()

    assert response.status_code == 200
    assert data[0]["id"] == random_id


# Тест фильтрации курсов по имени
@pytest.mark.django_db
def test_filter_by_name(client, courses_factory):
    # Создаем 99 курсов с помощью фикстуры courses_factory
    courses = courses_factory(_quantity=99)

    # Выбираем случайное имя из созданных курсов
    random_name = [i.name for i in courses][randint(0, 98)]

    # Отправляем GET-запрос для фильтрации курсов по случайному имени
    response = client.get(f"/api/v1/courses/?name={random_name}")
    data = response.json()

    assert response.status_code == 200
    assert data[0]["name"] == random_name


# Тест создания нового курса
@pytest.mark.django_db
def test_create_course(client):
    # Отправляем POST-запрос для создания нового курса
    response = client.post("/api/v1/courses/", {"name": "Python", "students": []})

    assert response.status_code == 201


# Тест обновления существующего курса
@pytest.mark.django_db
def test_update_course(client, courses_factory):
    # Создаем 10 курсов с помощью фикстуры courses_factory
    courses = courses_factory(_quantity=10)

    # Выбираем случайный ID из созданных курсов
    random_id = [i.id for i in courses][randint(0, 9)]

    # Отправляем PATCH-запрос для обновления случайного курса
    response = client.patch(f"/api/v1/courses/{random_id}/", {"name": "Python", "students": []})

    assert response.status_code == 200

    # Проверяем, что курс был успешно обновлен
    new_response = client.get(f"/api/v1/courses/{random_id}/")
    assert new_response.json()["name"] == "Python"


# Тест удаления курса
@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    # Создаем 10 курсов с помощью фикстуры courses_factory
    courses = courses_factory(_quantity=10)

    # Выбираем случайный ID из созданных курсов
    random_id = [i.id for i in courses][randint(0, 9)]

    # Отправляем DELETE-запрос для удаления случайного курса
    response = client.delete(f"/api/v1/courses/{random_id}/")

    assert response.status_code == 204
