# Generated by Django 3.2.25 on 2024-04-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]