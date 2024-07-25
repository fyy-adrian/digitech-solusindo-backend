# Generated by Django 5.0.6 on 2024-07-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_price_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('image', models.CharField(default='default.jpg', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='hero',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='title',
        ),
    ]
