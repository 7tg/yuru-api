# Generated by Django 2.1.2 on 2018-10-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(max_length=1)),
                ('passwd', models.CharField(max_length=255)),
            ],
        ),
    ]
