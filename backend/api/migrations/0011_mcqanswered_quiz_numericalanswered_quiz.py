# Generated by Django 4.2.11 on 2024-04-07 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_codingquestions_marks_codingquestions_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcqanswered',
            name='quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.quiz'),
        ),
        migrations.AddField(
            model_name='numericalanswered',
            name='quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.quiz'),
        ),
    ]
