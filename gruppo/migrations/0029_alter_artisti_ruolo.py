# Generated by Django 4.2.6 on 2023-12-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruppo', '0028_alter_artisti_ruolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisti',
            name='ruolo',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='gruppo.ruolo'),
        ),
    ]