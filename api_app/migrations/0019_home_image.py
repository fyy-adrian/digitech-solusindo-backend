# Generated by Django 5.0.6 on 2024-07-24 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0018_remove_home_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.FileField(default='default.jpg', max_length=255, upload_to=''),
        ),
    ]
