import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # # Открываем файл phones.csv для чтения
        with open('phones.csv', 'r') as file:
            # Создаем список словарей для хранения данных из CSV файла
            phones = list(csv.DictReader(file, delimiter=';'))
        # Проходим по каждому телефону в списке
        for phone in phones:
            # Создаем новый объект модели Phone
            new_phone = Phone(
                name=phone['name'],  # Имя телефона
                price=float(phone['price']),  # Цена телефона
                image=phone['image'],  # URL изображения
                release_date=phone['release_date'],  # Дата выпуска
                lte_exists=(phone['lte_exists'] == 'true'),  # Поддержка LTE
            )

            # Сохраняем новый объект в базу данных
            new_phone.save()

            # Выводим сообщение об успешном завершении импорта
            self.stdout.write(self.style.SUCCESS(f'Успешно добавлен телефон: {new_phone.name}'))

