# Generated by Django 4.0.2 on 2022-04-25 11:22

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_team_teamtranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='photos/about', verbose_name='Main Image')),
            ],
            options={
                'verbose_name': 'About Main Image',
                'verbose_name_plural': 'About Main Image',
            },
        ),
        migrations.CreateModel(
            name='Hitofsales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/about', verbose_name='Image 1')),
            ],
            options={
                'verbose_name': 'Hit Of Sales',
                'verbose_name_plural': 'Hit Of Sales',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutimages',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.RemoveField(
            model_name='aboutimages',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='aboutimages',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='aboutimages',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='aboutimages',
            name='main_image',
        ),
        migrations.AddField(
            model_name='aboutimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/about', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='AboutImagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='pages.aboutimages')),
            ],
            options={
                'verbose_name': 'About Translation',
                'db_table': 'pages_aboutimages_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
