# Generated by Django 3.2 on 2022-09-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
