# Generated by Django 3.2.25 on 2024-04-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_user_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_teamlead',
            field=models.BooleanField(default=False),
        ),
    ]
