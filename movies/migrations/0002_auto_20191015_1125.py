# Generated by Django 2.2.6 on 2019-10-15 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='gnere',
            new_name='genre',
        ),
    ]
