# Generated by Django 3.2.1 on 2021-05-06 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_app', '0008_subject_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='users',
        ),
        migrations.AddField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]