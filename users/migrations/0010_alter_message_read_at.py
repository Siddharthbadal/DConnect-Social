# Generated by Django 4.2.1 on 2023-06-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_message_read_at_alter_message_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='read_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
