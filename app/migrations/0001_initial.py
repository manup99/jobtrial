# Generated by Django 2.2 on 2019-10-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_heading', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('salary', models.IntegerField(default=10000)),
                ('apply_by', models.DateField()),
                ('job_type', models.CharField(max_length=255)),
                ('available', models.IntegerField()),
                ('about_company', models.TextField()),
                ('about_job', models.TextField()),
                ('skills', models.TextField()),
                ('requirements', models.TextField()),
                ('why_us', models.TextField()),
            ],
        ),
    ]
