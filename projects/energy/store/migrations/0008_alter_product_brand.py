# Generated by Django 4.0.2 on 2022-05-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.BooleanField(default=False, verbose_name='New'),
        ),
    ]
