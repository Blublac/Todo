# Generated by Django 3.2.9 on 2021-11-25 11:40

from django.db import migrations, models
import todos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default=todos.models.getday, max_length=50)),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
