# Generated by Django 3.2.5 on 2021-09-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
