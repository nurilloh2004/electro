# Generated by Django 4.0.2 on 2022-04-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_metawords'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta'),
        ),
    ]
