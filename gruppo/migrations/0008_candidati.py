# Generated by Django 4.2.6 on 2023-12-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0007_rename_foto_artisti_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('data_nascita', models.DateTimeField()),
                ('email', models.CharField(max_length=200)),
                ('eperienza', models.TextField()),
                ('strumento', models.CharField(max_length=200)),
            ],
        ),
    ]
