# Generated by Django 4.2.1 on 2023-06-07 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=datetime.datetime(2023, 6, 7, 9, 45, 35, 292953, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
