# Generated by Django 5.0.3 on 2024-03-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='swimmer',
            name='event',
        ),
    ]
