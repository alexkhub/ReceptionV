# Generated by Django 5.0.6 on 2024-06-01 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profession_level_of_education_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос поступающего', 'verbose_name_plural': 'Вопросы поступающих'},
        ),
    ]
