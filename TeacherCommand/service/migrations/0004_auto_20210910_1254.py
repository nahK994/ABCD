# Generated by Django 3.2.5 on 2021-09-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20210910_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherCommand',
            fields=[
                ('eventId', models.AutoField(primary_key=True, serialize=False)),
                ('teacherId', models.IntegerField()),
                ('userName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
