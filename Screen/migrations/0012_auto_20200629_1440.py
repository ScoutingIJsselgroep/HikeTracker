# Generated by Django 3.0.3 on 2020-06-29 14:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Screen', '0011_auto_20200629_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkpoint',
            name='location',
            field=models.CharField(default='', max_length=200, verbose_name='Location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False),
        ),
    ]
