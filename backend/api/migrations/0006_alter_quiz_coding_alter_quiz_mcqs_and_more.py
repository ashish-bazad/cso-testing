# Generated by Django 4.2.11 on 2024-03-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_quiz_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='coding',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='mcqs',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='numericals',
            field=models.BooleanField(default=False),
        ),
    ]