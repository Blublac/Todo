# Generated by Django 3.2.9 on 2021-11-28 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_passholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='passholder',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='passkey', to=settings.AUTH_USER_MODEL),
        ),
    ]
