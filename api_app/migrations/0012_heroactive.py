# Generated by Django 5.0.6 on 2024-07-18 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0011_delete_heroactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.hero')),
            ],
        ),
    ]
