# Generated by Django 5.1.1 on 2024-09-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="teacher",
        ),
        migrations.AlterField(
            model_name="student",
            name="group",
            field=models.CharField(max_length=10, verbose_name="Класс"),
        ),
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.CharField(max_length=10, verbose_name="Предмет"),
        ),
    ]
