# Generated by Django 5.0.6 on 2024-06-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_user_phone_specialist_text_user_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='position',
            field=models.CharField(choices=[('Глава приема', 'Глава приема'), ('Член приемной комиссии', 'Член приемной комиссии')], max_length=100, verbose_name='Должность'),
        ),
    ]
