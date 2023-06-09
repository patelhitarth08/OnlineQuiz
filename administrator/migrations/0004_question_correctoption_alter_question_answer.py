# Generated by Django 4.1.7 on 2023-05-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_alter_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correctOption',
            field=models.CharField(choices=[('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4')], default='option1', max_length=7),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]
