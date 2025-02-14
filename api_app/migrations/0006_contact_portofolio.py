# Generated by Django 5.0.6 on 2024-07-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_service_remove_hero_description_remove_hero_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('comment', models.CharField(default='default.jpg', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Portofolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='default.jpg', max_length=255)),
            ],
        ),
    ]
