# Generated by Django 3.2.18 on 2023-05-03 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_seller_categories'),
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuarios.seller'),
            preserve_default=False,
        ),
    ]
