# Generated by Django 5.0.1 on 2024-01-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codpi', '0006_alter_shop_brand_alter_shop_color_alter_shop_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='sportswear_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание спортивной одежды'),
        ),
    ]