# Generated by Django 5.1.4 on 2025-01-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
