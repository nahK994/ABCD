# Generated by Django 3.2.5 on 2021-09-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_remove_teachercommand_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachercommand',
            name='password',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]
