# Generated by Django 2.1.2 on 2018-10-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20181029_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=64),
        ),
    ]