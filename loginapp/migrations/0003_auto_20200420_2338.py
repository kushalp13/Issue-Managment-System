# Generated by Django 3.0.4 on 2020-04-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20200315_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='usertype',
            field=models.CharField(max_length=13),
        ),
    ]
