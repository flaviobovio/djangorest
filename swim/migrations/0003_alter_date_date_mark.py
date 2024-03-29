# Generated by Django 4.2.11 on 2024-03-13 22:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('swim', '0002_date_remove_swimmer_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meters', models.FloatField()),
                ('date', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='swim.date')),
                ('swimmer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='swim.swimmer')),
            ],
        ),
    ]
