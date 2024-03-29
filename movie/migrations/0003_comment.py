# Generated by Django 2.2.6 on 2019-10-15 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20191015_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True,
                        serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'comment',
                    models.CharField(max_length=50)
                ),
                (
                    'movie',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='movie.Movie'
                    )
                ),
            ],
        ),
    ]
