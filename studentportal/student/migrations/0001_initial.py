# Generated by Django 4.2.2 on 2023-07-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('ClassId', models.AutoField(primary_key=True, serialize=False)),
                ('TeacherName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentId', models.AutoField(primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=100)),
                ('StudentLoc', models.CharField(max_length=100)),
                ('Standard', models.CharField(max_length=100)),
                ('StudentAge', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TeacherId', models.AutoField(primary_key=True, serialize=False)),
                ('TeacherName', models.CharField(max_length=100)),
                ('TeacherLoc', models.CharField(max_length=100)),
                ('Division', models.CharField(max_length=100)),
                ('TeacherAge', models.IntegerField()),
            ],
        ),
    ]
