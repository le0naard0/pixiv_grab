# Generated by Django 2.2.16 on 2020-09-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grab', '0003_auto_20200929_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='tag',
            field=models.TextField(blank=True, null=True),
        ),
    ]
