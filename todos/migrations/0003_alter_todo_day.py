# Generated by Django 3.2.9 on 2021-11-23 11:55

from django.db import migrations, models
import todos.models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='day',
            field=models.CharField(default=todos.models.getday, max_length=50),
        ),
    ]
