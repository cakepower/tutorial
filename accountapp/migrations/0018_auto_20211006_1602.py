# Generated by Django 3.2.7 on 2021-10-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0017_auto_20211006_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='text',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
