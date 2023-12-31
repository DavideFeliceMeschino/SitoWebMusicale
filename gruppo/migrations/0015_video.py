# Generated by Django 4.2.6 on 2023-12-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0014_alter_commenti_commento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=150, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('data_inserimento', models.DateTimeField(auto_now_add=True)),
                ('data_modifica', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(default='no-image.png', upload_to='img_video/%Y/%m/%d/')),
            ],
        ),
    ]
