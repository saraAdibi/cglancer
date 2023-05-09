# Generated by Django 4.2 on 2023-05-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='لینک')),
                ('url_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان لینک')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'گالری',
                'verbose_name_plural': 'گالری',
            },
        ),
    ]
