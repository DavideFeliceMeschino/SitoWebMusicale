# Generated by Django 4.2.6 on 2023-12-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0026_artisti_ruolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruolo',
            name='nome',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
