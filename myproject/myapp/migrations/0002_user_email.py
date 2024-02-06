# Generated by Django 5.0.1 on 2024-02-05 12:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, unique=True),
            preserve_default=False,
        ),
    ]
