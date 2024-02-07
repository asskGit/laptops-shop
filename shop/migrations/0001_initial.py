# Generated by Django 5.0.1 on 2024-02-05 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(upload_to='laptop/')),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'laptop',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptops', to='shop.laptop')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
