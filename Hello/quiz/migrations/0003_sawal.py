# Generated by Django 4.0.6 on 2022-07-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_question_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='sawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sawal', models.CharField(choices=[('choice_1', 'Answer_1'), ('choice_2', 'Answer_2'), ('choice_3', 'Answer_3'), ('choice_4', 'Answer_4'), ('choice_5', 'Answer_5'), ('choice_6', 'Answer_6')], max_length=50, unique=True)),
                ('jawab', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]