# Generated by Django 4.1 on 2023-03-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('fathername', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
    ]