# Generated by Django 2.1.2 on 2018-10-29 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_campaign_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
            preserve_default=False,
        ),
    ]
