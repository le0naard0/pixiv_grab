# Generated by Django 2.2.16 on 2020-09-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grab', '0006_auto_20200929_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
