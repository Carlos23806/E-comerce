# Generated by Django 5.1.4 on 2025-01-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylog', '0003_alter_product_imgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='imgs',
            field=models.ImageField(blank=True, default='uploads/default_profile_picture.jpg', upload_to='uploads/UserProfile/'),
        ),
    ]
