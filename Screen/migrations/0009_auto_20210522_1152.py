# Generated by Django 3.2.3 on 2021-05-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Screen', '0008_alter_route_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='bonuspunten',
            field=models.IntegerField(default=0, verbose_name='Bonuspunten'),
        ),
        migrations.AddField(
            model_name='team',
            name='punten',
            field=models.IntegerField(default=0, verbose_name='Punten'),
        ),
        migrations.AddField(
            model_name='team',
            name='strafkilometers',
            field=models.IntegerField(default=0, verbose_name='Strafpunten'),
        ),
    ]
