# Generated by Django 3.2.5 on 2021-09-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20210919_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachercommand',
            name='aboutMe',
            field=models.CharField(default='null', max_length=80),
            preserve_default=False,
        ),
    ]