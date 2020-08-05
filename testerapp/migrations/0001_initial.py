# Generated by Django 3.0.4 on 2020-03-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugInfo',
            fields=[
                ('bugId', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('bugDesc', models.CharField(max_length=72)),
                ('currBuild', models.CharField(max_length=11)),
                ('dateRaised', models.DateField()),
                ('appName', models.CharField(max_length=11)),
                ('detectedBy', models.CharField(max_length=30)),
                ('bugStatus', models.CharField(max_length=6)),
                ('fixedBy', models.CharField(max_length=30)),
                ('bugPriority', models.CharField(max_length=7)),
            ],
        ),
    ]