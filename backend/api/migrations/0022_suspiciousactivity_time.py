# Generated by Django 4.2.11 on 2024-04-28 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_codingquestions_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspiciousactivity',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
