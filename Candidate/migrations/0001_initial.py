# Generated by Django 3.0 on 2020-03-20 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidateId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('total_experiences', models.FloatField()),
                ('total_skills', models.IntegerField()),
                ('designation', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('skills_score', models.FloatField()),
                ('experiences_skills_combined_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('resumeId', models.AutoField(primary_key=True, serialize=False)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
