# Generated by Django 5.1.4 on 2024-12-17 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_analyst', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'ordering': ['-created_at'], 'verbose_name': 'Имя', 'verbose_name_plural': 'Имена'},
        ),
        migrations.AddField(
            model_name='buyer',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2024, 12, 17), verbose_name='Имя'),
        ),
    ]
