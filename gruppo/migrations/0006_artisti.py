# Generated by Django 4.2.6 on 2023-12-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0005_alter_carousel_img_alter_eventi_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artisti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('data_nascita', models.DateField(verbose_name='Data di nascita')),
                ('strumento', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('esperienza', models.TextField()),
                ('foto', models.ImageField(default=None, upload_to='img_artisti', verbose_name='Foto Profilo')),
            ],
        ),
    ]
