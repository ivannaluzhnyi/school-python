# Generated by Django 3.2.1 on 2021-05-05 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_app', '0003_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
