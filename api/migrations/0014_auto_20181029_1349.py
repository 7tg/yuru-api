# Generated by Django 2.1.2 on 2018-10-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20181029_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='capacity_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='step',
            name='step',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]