# Generated by Django 2.1.4 on 2018-12-06 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_score_s_char'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('e_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=50)),
                ('e_time', models.DateTimeField()),
                ('e_pos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Exam')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
