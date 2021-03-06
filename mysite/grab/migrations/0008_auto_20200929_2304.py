# Generated by Django 2.2.16 on 2020-09-29 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grab', '0007_auto_20200929_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='author_load_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
