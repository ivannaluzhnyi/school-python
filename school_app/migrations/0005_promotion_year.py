# Generated by Django 3.2.1 on 2021-05-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0004_auto_20210505_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='year',
            field=models.IntegerField(default=1970),
            preserve_default=False,
        ),
    ]
