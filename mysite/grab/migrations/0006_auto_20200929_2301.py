# Generated by Django 2.2.16 on 2020-09-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grab', '0005_auto_20200929_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='NSFW',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
