# Generated by Django 4.2.6 on 2023-12-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0004_alter_carousel_img_alter_eventi_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.ImageField(default='media/logo.png', upload_to='slide/%Y/%m/%d', verbose_name='Immagine Slide'),
        ),
        migrations.AlterField(
            model_name='eventi',
            name='img',
            field=models.ImageField(default='media/logo.png', upload_to='img_evento/%Y/%m/%d', verbose_name='Immagine Evento'),
        ),
    ]
