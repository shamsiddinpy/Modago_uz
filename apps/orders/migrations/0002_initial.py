# Generated by Django 5.1.2 on 2024-10-19 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to='shops.currency'),
        ),
    ]
