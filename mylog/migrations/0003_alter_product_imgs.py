# Generated by Django 5.1.4 on 2025-01-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0002_alter_product_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imgs',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]