# Generated by Django 2.1.2 on 2018-10-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181029_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(max_length=64),
        ),
    ]