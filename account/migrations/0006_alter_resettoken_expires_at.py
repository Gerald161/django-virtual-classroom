# Generated by Django 4.1.7 on 2023-05-15 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_resettoken_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resettoken',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 19, 12, 44, 103681, tzinfo=datetime.timezone.utc)),
        ),
    ]
