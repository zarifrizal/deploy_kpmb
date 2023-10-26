# Generated by Django 4.2.4 on 2023-10-05 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('status', models.CharField(default='Active', max_length=8)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.course')),
            ],
        ),
    ]