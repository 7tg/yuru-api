# Generated by Django 2.1.2 on 2018-10-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20181029_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='date',
            field=models.DateField(),
        ),
    ]