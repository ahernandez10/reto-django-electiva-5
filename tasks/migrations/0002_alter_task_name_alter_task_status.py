# Generated by Django 4.1.1 on 2022-09-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=65, unique=True, verbose_name='Nombre De La Tarea'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('u', 'No Iniciada'), ('o', 'En Progreso'), ('f', 'Finalizada')], max_length=1, verbose_name='Estado'),
        ),
    ]
